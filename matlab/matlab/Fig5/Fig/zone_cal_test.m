function [area_update_ad,zone_mat_ad, mean_data_ad,std_data_ad,max_min_Zone]=zone_cal_test(stimulation_point,basal_window,Time_limit,area_update,zone_Data,mean_data,std_data,dest_folder,source_file)

zone_1=zone_Data(:,1:2);
zone_2=zone_Data(:,5:6);
zone_3=zone_Data(:,3:4);
zone_4=zone_Data(:,7:8);
updated_Zone=horzcat(zone_1,zone_2,zone_3,zone_4);
updated_Zone_rel=updated_Zone-stimulation_point;

updated_Zone_rel_d=updated_Zone_rel;

%for  k=1:size(updated_Zone_rel,1)
    updated_Zone_rel_d(:,2)=updated_Zone_rel_d(:,2)-updated_Zone_rel_d(:,1)+1;
    updated_Zone_rel_d(:,4)=updated_Zone_rel_d(:,4)-updated_Zone_rel_d(:,3)+1;
    updated_Zone_rel_d(:,6)=updated_Zone_rel_d(:,6)-updated_Zone_rel_d(:,5)+1;
    updated_Zone_rel_d(:,8)=updated_Zone_rel_d(:,8)-updated_Zone_rel_d(:,7)+1;

stimulation_Start=stimulation_point;%100;%100;
%Time_limit=190;

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
folders=dir(source_file);

temp_Result=[];
fold_cnt=0;
zone_third=[];
zone_mat_ad=[];
zone_mat_ad=updated_Zone_rel_d;
%area_update_ad=area_update;
%mean_data_ad=mean_data;
%std_data_ad=std_data;
area_update_ad=[];
mean_data_ad=[];
std_data_ad=[];
folder_zone_Data=[];
max_min_Zone=[];
%fold_cnt_temp=0;
 for i =3:length(folders)
    %fold_cnt=fold_cnt+1;
    folders_name= horzcat(source_file,folders(i).name);
    files = dir(horzcat(folders_name,'\*SingleTrial_GPI_FR*.csv'));
        for j=1:length(files)
            fold_cnt=fold_cnt+1;
            current_file_name=horzcat(folders_name,'\',files(j).name);
            GP_FR=[];
            data_mean=[];
            data_mean_multi=[];
            [GP_FR,T,vT]=xlsread(current_file_name) ; 

            
             %if (i<5)
                    basal_FR=mean2(GP_FR(:,600:699)); 
                    basal_FR_std = std2(GP_FR(:,600:699));
                    tempGP_FR= GP_FR;
                    GP_FR =[];
                    GP_FR = tempGP_FR(:,600:950);
            %else
            %        basal_FR=mean2(GP_FR(:,1:basal_window)); 
            %        basal_FR_std = std2(GP_FR(:,1:basal_window));
            %end
            
            
            GP_FR_mean=mean(GP_FR);            
             bin_p_z=ones(Time_limit,1)*100;
             bin_pp_z=ones(Time_limit,1)*100;
             bin_ci_z=ones(Time_limit,1)*1000;
             bin_ci_zstat=ones(Time_limit,2)*1000;
             %basal_FR=30;
            for k=stimulation_Start+1:Time_limit%bin index
                 trial_Data_in_bin=access_data_for_each_bin_trial(GP_FR,k);
                 [h_z,p_z,ci_z,zval_z] = ztest(trial_Data_in_bin,basal_FR,basal_FR_std);
                 bin_p_z(k,1)=h_z;
                 bin_pp_z(k,1)=p_z;
                 bin_ci_z(k,1)=zval_z;

            end
              
                           
              %%%%%%%%%%%%%%%%%%firstexcitationend %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
              %first_excitation=updated_Zone_rel_d(fold_cnt,1)+updated_Zone_rel_d(fold_cnt,2);
              zone_index=1;
              flag1=check_next_gap(zone_mat_ad,fold_cnt,zone_index);
              if(flag1==1)
                                    temp_mag=[];
                                    start_bin=stimulation_Start+updated_Zone_rel_d(fold_cnt,zone_index);
                                    zone_index=1;
                                    next_start=stimulation_Start+updated_Zone_rel_d(fold_cnt,zone_index+2) ;
                                    %end_bin=previous_end_bin;
                                    %if(bin_ci(next_start-1)>0)% fall in early excitation
                                    if(bin_p_z(next_start-1)==1)% fall in early excitation
                                           end_bin=next_start-1;    
%                                             for kk=start_bin: end_bin
%                                                 temp_mag=horzcat(temp_mag,GP_FR_mean(1,kk)); 
%                                             end
                                            zone_mat_ad(fold_cnt,2)=updated_Zone_rel_d(fold_cnt,2)+1;
                                    else                 % else fall in first inhibition 
                                        disp('else do nothing')
                                    end
              else
              end
              %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%for first inhbition%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
              zone_index=3;
              flag2_previous=check_previous_gap(updated_Zone_rel_d,fold_cnt,zone_index);
              if(flag2_previous==1)
                  start_bin=stimulation_Start+updated_Zone_rel_d(fold_cnt,zone_index)-1;  
                  if(bin_ci_z(start_bin)<0)% start falls in inhibition
                                            temp_mag=[];
                                           previous_end_bin=updated_Zone_rel_d(fold_cnt,zone_index+1)+start_bin;
%                                            for kk=start_bin: previous_end_bin
%                                                 temp_mag=horzcat(temp_mag,GP_FR_mean(1,kk)); 
%                                            end
                                            zone_mat_ad(fold_cnt,3)=start_bin-stimulation_Start;
                                            zone_mat_ad(fold_cnt,4)=updated_Zone_rel_d(fold_cnt,4)+1;                                          
                  else % start falls in early excitation
                     disp('else do nothing');
                  end                 
              else%same as previous
                 disp('else do nothing');
              end   
              flag2_next=check_next_gap(zone_mat_ad,fold_cnt,zone_index);
              if(flag2_next==1)
                                                                                                
                                   % end_bin=check_end_bin(updated_Zone_rel_d,fold_cnt,zone_index,bin_ci);
                                    next_start=stimulation_Start+updated_Zone_rel_d(fold_cnt,zone_index+2) ;
                                    end_bin=stimulation_Start+zone_mat_ad(fold_cnt,3)+zone_mat_ad(fold_cnt,4);
                                    diff_bin=next_start-end_bin;
                                    %end_bin=previous_end_bin;
                                    for m=next_start-diff_bin:next_start-1
                                        if(bin_ci_z(m)<0)% fall in late excitation
                                                temp_mag=[]
                                                %end_bin=next_start-1;    
                                                zone_mat_ad(fold_cnt,4)=zone_mat_ad(fold_cnt,4)+1;

                                        else                 % else fall in first inhibition  
                                               disp('else do nothing');
                                        end
                                    end
              else
                 disp('else do nothing');
              end
              
              %%%%%%%%%%%%for late excitation%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
              zone_index=5;
              flag2_previous=check_previous_gap(zone_mat_ad,fold_cnt,zone_index);
              
              if(flag2_previous==1)
                                        
                                           start_bin=stimulation_Start+updated_Zone_rel_d(fold_cnt,zone_index)-1;  
                                           if(bin_ci_z(start_bin)>0)% start falls in late excitation
                                               temp_mag=[];
%                                               previous_end_bin=zone_mat_ad(fold_cnt,zone_index+1)+start_bin;
%                                                for kk=start_bin: previous_end_bin
%                                                     temp_mag=horzcat(temp_mag,GP_FR_mean(1,kk)); 
%                                                end
                                                zone_mat_ad(fold_cnt,5)=start_bin-stimulation_Start;
                                                zone_mat_ad(fold_cnt,6)=updated_Zone_rel_d(fold_cnt,6)+1;
%                                                 area_update_ad(fold_cnt,3)=sum(temp_mag);
%                                                 mean_data_ad(fold_cnt,3)=mean(temp_mag);
%                                                 std_data_ad(fold_cnt,3)=std(temp_mag);
%                                                 folder_zone_Data{fold_cnt,3}=temp_mag;
                                           else%falls in early inhibition
                                              disp('else do nothing');
                                           end
              else%same as previous
                  disp('else do nothing');
              end   
              flag2_next=check_next_gap(zone_mat_ad,fold_cnt,zone_index);
              if(flag2_next==1)
                                   temp_mag=[];                                                                   
                                   % end_bin=check_end_bin(updated_Zone_rel_d,fold_cnt,zone_index,bin_ci);
                                    start_bin=stimulation_Start+zone_mat_ad(fold_cnt,zone_index); 
                                    original_end=start_bin+zone_mat_ad(fold_cnt,zone_index+1);
                                    next_start=stimulation_Start+updated_Zone_rel_d(fold_cnt,zone_index+2) ;
                                    %end_bin=previous_end_bin;
                                    diff_bin=next_start-original_end;
                                    for m=next_start-diff_bin:next_start-1
                                            if(bin_ci_z(m)>0)% fall in late excitation                                         
                                                    %end_bin=next_start-1;    
                                                    zone_mat_ad(fold_cnt,6)=zone_mat_ad(fold_cnt,6)+1;
                                            else                 % else fall in second inhibition                                         
                                                  disp('else do nothing');
                                            end
                                    end
              else
                 disp('else do nothing');
              end
                                       
              %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%late inhibition%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            if (zone_mat_ad(fold_cnt,7)>0)   
              zone_index=7;
              flag4_previous=check_previous_gap(zone_mat_ad,fold_cnt,zone_index);
              temp_mag=[];
              if(flag4_previous==1)
                    temp_mag=[];
                    original_start=stimulation_Start+zone_mat_ad(fold_cnt,zone_index);
                    original_end=stimulation_Start+zone_mat_ad(fold_cnt,zone_index-2)+zone_mat_ad(fold_cnt,zone_index-1);
                    diff_bin=original_start-original_end;
                    start_bin=stimulation_Start+updated_Zone_rel_d(fold_cnt,zone_index)-diff_bin;  
                    %if(bin_ci(start_bin)<0)% start falls in inhibition
                                           previous_end_bin=updated_Zone_rel_d(fold_cnt,zone_index+1)+start_bin;

                                            zone_mat_ad(fold_cnt,7)=start_bin-stimulation_Start;
                                            zone_mat_ad(fold_cnt,8)=updated_Zone_rel_d(fold_cnt,8)+diff_bin;
                    %else
                    %    disp('else do nothing');
                    %end
              else%same as previous
                 disp('else do nothing');
              end
            else
                disp ('thre is no zone separation')
            end
              %%%%%%%%%%%%%%%%%%%%%%%%%%%%area, mean, std calculation%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

                  start_bin=stimulation_Start+zone_mat_ad(fold_cnt,1);
                  end_bin=zone_mat_ad(fold_cnt,1)+zone_mat_ad(fold_cnt,2)+stimulation_Start-1;
                  temp_mag=GP_FR_mean(start_bin:end_bin);
                  area_update_ad(fold_cnt,1)=sum(temp_mag);
                  mean_data_ad(fold_cnt,1)=mean(temp_mag);
                  std_data_ad(fold_cnt,1)=std(temp_mag);
                  folder_zone_Data{fold_cnt,1}=temp_mag;
                  max_min_Zone(fold_cnt,1)=max(temp_mag);

                  
                  start_bin=stimulation_Start+zone_mat_ad(fold_cnt,3);
                  end_bin=zone_mat_ad(fold_cnt,3)+zone_mat_ad(fold_cnt,4)+stimulation_Start-1;
                  temp_mag=GP_FR_mean(start_bin:end_bin);
                  area_update_ad(fold_cnt,2)=sum(temp_mag);
                  mean_data_ad(fold_cnt,2)=mean(temp_mag);
                  std_data_ad(fold_cnt,2)=std(temp_mag);
                  folder_zone_Data{fold_cnt,2}=temp_mag;
                  max_min_Zone(fold_cnt,2)=min(temp_mag);
                  
                  start_bin=stimulation_Start+zone_mat_ad(fold_cnt,5);
                  end_bin=zone_mat_ad(fold_cnt,5)+zone_mat_ad(fold_cnt,6)+stimulation_Start-1;
                  temp_mag=GP_FR_mean(start_bin:end_bin);
                  area_update_ad(fold_cnt,3)=sum(temp_mag);
                  mean_data_ad(fold_cnt,3)=mean(temp_mag);
                  std_data_ad(fold_cnt,3)=std(temp_mag);
                  folder_zone_Data{fold_cnt,3}=temp_mag;
                  max_min_Zone(fold_cnt,3)=max(temp_mag);
                
                 if (zone_mat_ad(fold_cnt,7)>0) 
                  start_bin=stimulation_Start+zone_mat_ad(fold_cnt,7);
                  end_bin=zone_mat_ad(fold_cnt,7)+zone_mat_ad(fold_cnt,8)+stimulation_Start-1;
                  temp_mag=GP_FR_mean(start_bin:end_bin);
                  area_update_ad(fold_cnt,4)=sum(temp_mag);
                  mean_data_ad(fold_cnt,4)=mean(temp_mag);
                  std_data_ad(fold_cnt,4)=std(temp_mag);
                  folder_zone_Data{fold_cnt,4}=temp_mag;
                  max_min_Zone(fold_cnt,4)=min(temp_mag);
                 else
                  area_update_ad(fold_cnt,4)=0;
                  mean_data_ad(fold_cnt,4)=0;
                  std_data_ad(fold_cnt,4)=0;
                  folder_zone_Data{fold_cnt,4}=0;
                  max_min_Zone(fold_cnt,4)=0;
                 end
              %%%%%%%%%%%%%%%%%%%%%%visualize_update%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
             f = figure('Position', get(0, 'Screensize'));
             X_data = 1:length(GP_FR_mean);
             %%y_data=ones(1,200);
             f=bar(X_data,GP_FR_mean)  ;
             set(f,'FaceColor','c');                       
             grid on
             grid minor             
             hold on
             y = ylim;
             zone_name_start=1;
             x1=[zone_mat_ad(fold_cnt,1)+stimulation_Start zone_mat_ad(fold_cnt,1)+stimulation_Start];
             plot(x1,y,'color','r','Linewidth',1,'DisplayName', num2str(zone_name_start))
             x1=[zone_mat_ad(fold_cnt,1)+zone_mat_ad(fold_cnt,2)+stimulation_Start-1 zone_mat_ad(fold_cnt,1)+zone_mat_ad(fold_cnt,2)+stimulation_Start-1];
             plot(x1,y,'color','k','Linewidth',1,'DisplayName', num2str(zone_name_start))
             
             zone_name_start=2;
             x1=[zone_mat_ad(fold_cnt,3)+stimulation_Start zone_mat_ad(fold_cnt,3)+stimulation_Start];
             plot(x1,y,'color','r','Linewidth',1,'DisplayName', num2str(zone_name_start))
             x1=[zone_mat_ad(fold_cnt,3)+zone_mat_ad(fold_cnt,4)+stimulation_Start-1 zone_mat_ad(fold_cnt,3)+zone_mat_ad(fold_cnt,4)+stimulation_Start-1];
             plot(x1,y,'color','k','Linewidth',1,'DisplayName', num2str(zone_name_start))
             
             zone_name_start=3;
             x1=[zone_mat_ad(fold_cnt,5)+stimulation_Start zone_mat_ad(fold_cnt,5)+stimulation_Start];
             plot(x1,y,'color','r','Linewidth',1,'DisplayName', num2str(zone_name_start))
             x1=[zone_mat_ad(fold_cnt,5)+zone_mat_ad(fold_cnt,6)+stimulation_Start-1 zone_mat_ad(fold_cnt,5)+zone_mat_ad(fold_cnt,6)+stimulation_Start-1];
             plot(x1,y,'color','k','Linewidth',1,'DisplayName', num2str(zone_name_start))

             
             
             if (zone_mat_ad(fold_cnt,7)>0) 
             zone_name_start=4;
             x1=[zone_mat_ad(fold_cnt,7)+stimulation_Start zone_mat_ad(fold_cnt,7)+stimulation_Start];
             plot(x1,y,'color','r','Linewidth',1,'DisplayName', num2str(zone_name_start))
             x1=[zone_mat_ad(fold_cnt,7)+zone_mat_ad(fold_cnt,8)+stimulation_Start-1 zone_mat_ad(fold_cnt,7)+zone_mat_ad(fold_cnt,8)+stimulation_Start-1];
             plot(x1,y,'color','k','Linewidth',1,'DisplayName', num2str(zone_name_start))
                sub_dest_path=horzcat(dest_folder,folders(i).name);
                mkdir(sub_dest_path)
                dest_path=strcat(sub_dest_path,'\', num2str(fold_cnt),'final.png');
                saveas(f,dest_path) ;
             else
                sub_dest_path=horzcat(dest_folder,folders(i).name);
                mkdir(sub_dest_path)
                dest_path=strcat(sub_dest_path,'\', num2str(fold_cnt),'final_miss.png');
                saveas(f,dest_path) ;
             end
              close all;
              %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%  
       end
 end
 end

 function data_bin=access_data_for_each_bin_trial(GP_FR,index_bin);
             for k=1:size(GP_FR,1)
                data_bin(k,1)=GP_FR(k,index_bin);           
             end
 end
 
 function flag=check_previous_gap(updated_Zone_rel_d,fold_cnt,zone_index)
 first_inhibition=updated_Zone_rel_d(fold_cnt,zone_index);
 if(updated_Zone_rel_d(fold_cnt,zone_index-1)+updated_Zone_rel_d(fold_cnt,zone_index-2)-first_inhibition~=0)
     disp('there is a gap');
     flag=1;
 else
     flag=0;
 end
 end
 
 function flag=check_next_gap(updated_Zone_rel_d,fold_cnt,zone_index)
 first_inhibition=updated_Zone_rel_d(fold_cnt,zone_index)+updated_Zone_rel_d(fold_cnt,zone_index+1);
 if(updated_Zone_rel_d(fold_cnt,zone_index+2)-first_inhibition~=0)
     disp('there is a gap');
     flag=1;
 else
     flag=0;
 end
 end
 