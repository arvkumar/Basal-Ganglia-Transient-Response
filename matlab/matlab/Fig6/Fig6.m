function Fig6()

close all;

%source_Folder_single='S:\officeWork\2020\OFFICE\transient_Analysis_statistics\AprilData16\16thAprilFigure6_100Trials\16thAprilRestoration100Trials\';

source_Folder_single='\16thAprilRestoration100Trials\';
source_Folder_mean=source_Folder_single;
dest_folder='\16thAprilRestoration100Trialsoutput\';
dest_folder1='\16thAprilRestoration100Trialsoutput\';


mkdir(dest_folder)
mkdir(dest_folder1)
%basal_winodw=690;%90;
stimulation_Start=700;%100;
Time_limit=700+150;

loop_basal=[];
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
zone_data_temp1='result_zone_Temp1.txt';
zone_data_temp2='result_zone_Temp2.txt';
area_data_temp1='result_area_Temp1.txt';
area_data_temp2='result_area_Temp2.txt';

basal_FR_zone='basal_FR.txt';
basal_FR_zone_array=[];

std_data_temp2='result_area_std2.txt';
skew_data_temp2='result_area_skew2.txt';
mean_data_temp2='result_area_mean2.txt';

fp1=fopen(horzcat(dest_folder,zone_data_temp1),'w');
fq1=fopen(horzcat(dest_folder,area_data_temp1),'w');

fp2=fopen(horzcat(dest_folder,zone_data_temp2),'w');
fq2=fopen(horzcat(dest_folder,area_data_temp2),'w');

fq3=fopen(horzcat(dest_folder,std_data_temp2),'w');
fq4=fopen(horzcat(dest_folder,skew_data_temp2),'w');
fq5=fopen(horzcat(dest_folder,mean_data_temp2),'w');

fs=fopen(horzcat(dest_folder,'result_file_name.txt'),'w');
folders=dir(source_Folder_single);
folders_mean=dir(source_Folder_mean);

temp_Result=[];
fold_cnt=0;
zone_third=[];


for i =3:length(folders)
    fold_cnt=fold_cnt+1;
    folders_name= horzcat(source_Folder_single,folders(i).name);
    files = dir(horzcat(folders_name,'\*SingleTrial_GPI_FR*.csv'));
    fprintf(fs,'%s',folders(i).name);
    fprintf(fs,'\n');
    %folders_name_mean= horzcat(source_Folder_mean,folders_mean(i).name);
    %files_mean = dir(horzcat(folders_name_mean,'\*MultiTrial*.csv'));
       for j=1:1%length(files)
            xls_file=files(j).name;
            xls_file_name=horzcat(folders_name,'\',xls_file);
            GP_FR=[];
            data_mean=[];
            data_mean_multi=[];
            [v,T,vT]=xlsread(xls_file_name) ; 
                       if(size(vT,1)>100)
                start=2;
                cnt=0;
                for k=start:size(vT,1)
                    cnt=cnt+1;
                    for kk=1:size(vT,2)
                        GP_FR{cnt,kk}=vT{k,kk};                    
                    end
                end
            else
                for k=1:size(vT,1)
                    for kk=1:size(vT,2)
                    GP_FR{k,kk}=vT{k,kk};                    
                    end
                end
            end
            
            %%estimate_mean and std form trial data
            for k=1:size(GP_FR,1)
                %data_mean(k,:)=GP_FR{1,k}(1:basal_winodw); 
                kk =0;
                for roi=600:699%1:basal_winodw 
                      kk = kk+1;
                     data_mean(k,kk)=GP_FR{k,roi};

                end
            end
            %%estimate full 
            for k=1:size(GP_FR,1)
               %data_mean_multi(k,:)=GP_FR{1,k}(1:200); 
                for kk=1:Time_limit
                     data_mean_multi(k,kk)=GP_FR{k,kk}; 
                end
            end
            GP_FR_mean=mean(data_mean_multi);
            
            %mean_v=mean(mean(data_mean));
            %mean_v=median(mean(data_mean));
            basal_FR=mean2(data_mean);
            %basal_FR=mean_v;
            %std_v=mean(std(data_mean));
            basal_FR_std = std2(data_mean);
            loop_basal(fold_cnt,1)=basal_FR;

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
            basal_FR_zone_array(fold_cnt,1)=basal_FR;
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
folder_plot_name=folders(i).name;
file_plot_name=xls_file;
%[temp_Result_ex,temp_Result_in,area_zone]=zone_Demarkation(Time_limit,stimulation_Start,GP_FR_mean,bin_ci,bin_p,dest_folder,folder_plot_name,file_plot_name);
[temp_Result_ex,temp_Result_in,area_zone]=zone_Demarkation(Time_limit,stimulation_Start,GP_FR_mean,bin_ci_z,bin_p_z,dest_folder,folder_plot_name,file_plot_name);

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
     %fprintf(fp,'%s', xls_file);
      for jjj=1:1%size(temp_Result_ex,2)
           if(length(temp_Result_ex{1,jjj})~=0)
                fprintf(fp1,' %s ', num2str(temp_Result_ex{1,jjj}));
           end
      end
      for jjj=1:1%size(temp_Result_in,2)
          if(length(temp_Result_in{1,jjj})~=0)
            fprintf(fp1,' %s ', num2str(temp_Result_in{1,jjj}));  
          end
      end
       for jjj=1:1%size(area_zone,2)
            if(length(area_zone{1,jjj})~=0)
            fprintf(fq1,' %s ', num2str(area_zone{1,jjj}));  
          end 
       end
    
     fprintf(fp1,'\n');
     fprintf(fq1,'\n');
     close all;
       
  
%%late excitation and late inhibtion detection
%[temp_Result_ex1,temp_Result_in1,area_zone1,std_zone1,skew_Zone1,mean_Zone1,third_zone_Data]=late_zone_Demarcation_II(Time_limit,stimulation_Start,GP_FR_mean,bin_ci,bin_p,bin_pp,dest_folder,folder_plot_name,file_plot_name,temp_Result_ex,temp_Result_in);
[temp_Result_ex1,temp_Result_in1,area_zone1,std_zone1,skew_Zone1,mean_Zone1,third_zone_Data]=late_zone_Demarcation_II(Time_limit,stimulation_Start,GP_FR_mean,bin_ci_z,bin_p_z,bin_pp_z,dest_folder,folder_plot_name,file_plot_name,temp_Result_ex,temp_Result_in);

%%[temp_Result_ex1,temp_Result_in1,area_zone1]=late_zone_Demarcation_III(Time_limit,stimulation_Start,GP_FR_mean,bin_ci,bin_p,dest_folder,folder_plot_name,file_plot_name,temp_Result_ex,temp_Result_in);
zone_third{fold_cnt}=third_zone_Data;
third_zone_Data=[];
  for jjj=1:1%size(temp_Result_ex,2)
           if(length(temp_Result_ex1{1,jjj})~=0)
                fprintf(fp2,' %s ', num2str(temp_Result_ex1{1,jjj}));
           end
      end
  for jjj=1:2%size(temp_Result_in,2)
      if(length(temp_Result_in{1,jjj})~=0)
        fprintf(fp2,' %s ', num2str(temp_Result_in1{1,jjj}));  
      end
  end
   for jjj=1:3%size(area_zone,2)
        if(length(area_zone1{1,jjj})~=0)
        fprintf(fq2,' %s ', num2str(area_zone1{1,jjj})); 
        fprintf(fq3,' %s ', num2str(std_zone1{1,jjj})); 
        fprintf(fq4,' %s ', num2str(skew_Zone1{1,jjj})); 
        fprintf(fq5,' %s ', num2str(mean_Zone1{1,jjj})); 
      end 
   end
   

   
     temp_Result_ex=[];
     temp_Result_in=[];
     %magnitude_zone=[];
     area_zone=[];
     temp_Result_ex1=[];
     temp_Result_in1=[];
     area_zone1=[];
     std_zone1=[];
     skew_Zone1=[];
     mean_Zone1=[];
     fprintf(fp2,'\n');
     fprintf(fq2,'\n');
     fprintf(fq3,'\n');
     fprintf(fq4,'\n');
     fprintf(fq5,'\n');
     close all;
     
       end
%  fprintf(fp,'%s', folders(i).name);
%  fprintf(fp,'\n');
 end
 fclose(fs);
 fclose(fp1);
 fclose(fq1);
 fclose(fp2);
 fclose(fq2);
 fclose(fq3);
 fclose(fq4);
 fclose(fq5);
 disp('end')
 
 file_name_disconnection=horzcat(dest_folder,'result_file_name.txt');

 area_file1=horzcat(dest_folder,area_data_temp1);
 zone_file_name1=horzcat(dest_folder,zone_data_temp1);

 area_file2=horzcat(dest_folder,area_data_temp2);
 zone_file_name2=horzcat(dest_folder,zone_data_temp2);
 std_file_name2=horzcat(dest_folder,std_data_temp2);
 %skew_file_name2=horzcat(dest_folder,skew_data_temp2);
 mean_file_name2=horzcat(dest_folder, mean_data_temp2);
 
 output_file_name1='tempx2_dist.xls';
 output_file_name2='tempx2_zone.xls';
 zone_std2=load(std_file_name2);
 %zone_skwe2=load(skew_file_name2);
 zone_mean2=load(mean_file_name2);
 
 [area_update,zone_update]=post_process_Data(area_file1,zone_file_name1,area_file2,zone_file_name2); 
 
[area_update_ad,zone_update_ad,mean_ad,std_ad,max_min_Zone]=zone_cal_test(stimulation_Start,Time_limit,area_update,zone_update,zone_mean2,zone_std2,dest_folder,source_Folder_single); 
 num='method';
 %durationmat=zone_update_ad(:,2:2:8);
%area_update_ad=area_update_ad./durationmat;
feature_Calculate(dest_folder1,zone_third,area_update_ad,zone_update_ad,std_ad,mean_ad,max_min_Zone,basal_FR_zone_array,file_name_disconnection,stimulation_Start,output_file_name1,output_file_name2,num);%working
 
xls_data = [zone_update_ad(:,1:2:8) zone_update_ad(:,2:2:8)  area_update_ad, mean_ad, std_ad, max_min_Zone];
xlswrite('feature.xlsx',xls_data)
end



function [mean_latency_duration,std_latency_duration,mean_area,std_area,mean_basal,std_basal]=mean_Std(zone_latency_duration,zone_mean_area,basal_mean_multi2,basal_std_multi2)

mean_latency_duration=mean(zone_latency_duration);
std_latency_duration=std(zone_latency_duration);
mean_area=mean(zone_mean_area);
std_area=std(zone_mean_area);
mean_basal=mean(basal_mean_multi2);
std_basal=std(basal_std_multi2);

end

function [area_update,zone_update]=post_process_Data(area_file1,zone_file_name1,area_file2,zone_file_name2)
area1=load(area_file1);
zone1=load(zone_file_name1);
area2=load(area_file2);
zone2=load(zone_file_name2);

area_update=horzcat(area1(:,1),area2(:,1:3));
zone_update=horzcat(zone1(:,1:2),zone2(:,1:6));
end



function data_bin=access_data_for_each_bin_trial(GP_FR,index_bin);
             for k=1:size(GP_FR,1)
                data_bin(k,1)=GP_FR{k,index_bin};           
             end
end



function [temp_Result_ex,temp_Result_in,area_zone,std_zone,skew_Zone,mean_zone,third_zone_Data]=late_zone_Demarcation_II(Time_limit,stimulation_Start,GP_FR_mean,bin_ci,bin_p,bin_pp,dest_folder,folder_plot_name,file_plot_name,temp_Result_ex,temp_Result_in)

            
 f = figure('Position', get(0, 'Screensize'));
 X_data = 1:length(GP_FR_mean);
 %%y_data=ones(1,200);
 f=bar(X_data,GP_FR_mean)  ;
 set(f,'FaceColor','c');                       
 grid on
 grid minor             
 hold on
 y = ylim;

k=temp_Result_ex{1,1}(2)+1;%%%stimulation_Start;
%temp_k=k;
word_cnt_ex=0;
word_cnt_in=0;
zone_mark=0;
early_flag=0;
temp_Result_ex=[];
temp_Result_in=[];
magnitude_zone=[];
area_zone=[];
std_zone=[];
mean_zone=[];
third_zone_Data=[];
            while(k<=Time_limit-40) 
                 cnt_early=1;
                 temp_mag=[];
                  if((bin_p(k,1)==1)&(bin_p(k+1,1)==1))
                  %if(bin_ci(k,1)>0)&&(bin_ci(k+1,1)>0)%excitated start
                       %if(bin_ci(k,1)>4)&&(bin_ci(k+1,1)>4)%excitated start
                       if(bin_ci(k,1)>1)&&(bin_ci(k+1,1)>1)%excitated start with STN col
                              early_flag=1;
                              if(cnt_early==1)
                                  x1 = [k k];                     
                                  zone_mark=zone_mark+1;
                                  zone_start_bin=k;
                                  
                                  
                                  zone_name_start=horzcat(num2str(zone_mark),' zone start', ' bin ',num2str(k));
                                  plot(x1,y,'color','r','Linewidth',1,'DisplayName', zone_name_start)
                                  text(x1(2)-1,y(2),num2str(zone_mark),'Fontsize',12)   
                                  
                              end
                              for kk=k:Time_limit-40                       
                                    if((bin_ci(kk,1)>0)&&(bin_ci(kk+1,1)>0)&&(bin_p(kk,1)==1)&(bin_p(kk+1,1)==1))&&(kk<=Time_limit-40)
                                         disp('continue');
                                         temp_mag=horzcat(temp_mag,GP_FR_mean(1,kk));
                                         
                                         cnt_early=cnt_early+1;
                                    elseif ((bin_ci(kk+1,1)<0)&&(bin_ci(kk+2,1)<0)||(bin_p(kk+1,1)~=1)&(bin_p(kk+2,1)~=1))
                                        x1 = [kk kk];
                                        zone_end_bin=kk;
                                        temp_mag=horzcat(temp_mag,GP_FR_mean(1,kk));
                                        
                                        zone_name_end=horzcat(num2str(zone_mark),' zone end',' bin ',num2str(kk));
                                        plot(x1,y,'color','k','Linewidth',1,'DisplayName', zone_name_end);
                                        text(x1(2)-1,y(2),num2str(zone_mark),'Fontsize',12);  
                                        %temp_Result_ex{fold_cnt,zone_mark}=[zone_start_bin zone_end_bin]; 
                                        word_cnt_ex=word_cnt_ex+1;
                                        temp_Result_ex{1,word_cnt_ex}=[zone_start_bin zone_end_bin];    
                                        magnitude_zone{1,zone_mark}=temp_mag;
                                        area_zone{1,zone_mark}=sum(temp_mag);%*(zone_end_bin-zone_start_bin+1);
                                        std_zone{1,zone_mark}=std(temp_mag);
                                        skew_Zone{1,zone_mark} = skewness(temp_mag);
                                        mean_zone{1,zone_mark} =mean(temp_mag);
                                        if(zone_mark==2)
                                            third_zone_Data{1,1}=temp_mag;
                                        end
                                        break;
                                    end
                              end
                       else%%for inhibition
                         if(length(temp_Result_in)<1)
                            if((bin_ci(k,1)<0)&&(bin_ci(k+1,1)<0))%inhibited start
                               early_flag=0;
                               if(cnt_early==1)
                                  x1 = [k k];                     
                                  zone_mark=zone_mark+1;
                                  zone_start_bin=k;
                                  zone_name_start=horzcat(num2str(zone_mark),' zone start', ' bin ',num2str(k));
                                  plot(x1,y,'color','r','Linewidth',1,'DisplayName', zone_name_start)
                                  text(x1(2)-1,y(2),num2str(zone_mark),'Fontsize',12)                                    
                              end
                              for kk=k:Time_limit -40  
%                                    if(kk==152)
%                                        keyboard;
%                                    end
                                    if((bin_ci(kk,1)<0)&&(bin_ci(kk+1,1)<0)&&(bin_p(kk,1)==1)&(bin_p(kk+1,1)==1))
                                         disp('continue');
                                         temp_mag=horzcat(temp_mag,GP_FR_mean(1,kk));
                                         cnt_early=cnt_early+1;
                                    elseif(((bin_ci(kk+1,1)>0)&&(bin_ci(kk+1,1)>0)||(bin_p(kk+2,1)~=1)&(bin_p(kk+2,1)~=1))) && length(temp_Result_in) < 1
                                        x1 = [kk kk];
                                        zone_end_bin=kk;
                                        temp_mag=horzcat(temp_mag,GP_FR_mean(1,kk));
                                        
                                        zone_name_end=horzcat(num2str(zone_mark),' zone end',' bin ',num2str(kk));
                                        plot(x1,y,'color','k','Linewidth',1,'DisplayName', zone_name_end);
                                        text(x1(2)-1,y(2),num2str(zone_mark),'Fontsize',12);
                                        word_cnt_in=word_cnt_in+1;
                                        %temp_Result_in{fold_cnt,zone_mark}=[zone_start_bin zone_end_bin]; 
                                        temp_Result_in{word_cnt_in}=[zone_start_bin zone_end_bin];
                                        magnitude_zone{1,zone_mark}=temp_mag;
                                        area_zone{1,zone_mark}=sum(temp_mag);%*(zone_end_bin-zone_start_bin+1);
                                        std_zone{1,zone_mark}=std(temp_mag);
                                        skew_Zone{1,zone_mark} = skewness(temp_mag);
                                        mean_zone{1,zone_mark} =mean(temp_mag);
                                        break;
                                        elseif (((bin_ci(kk+1,1)>0)&&(bin_ci(kk+2,1)>0)|| (bin_pp(kk+2,1)>.001)&&(bin_pp(kk+1,1)>.001)||(bin_p(kk+1,1)~=1)&(bin_p(kk+2,1)~=1))) && length(temp_Result_in) >=1 
                                        %elseif (((bin_ci(kk+1,1)>0)&&(bin_ci(kk+2,1)>0)||(bin_p(kk+1,1)~=1)&(bin_p(kk+2,1)~=1))) && length(temp_Result_in) >=1                   
                                        count_inh = 1;
                                         for l = kk+1:kk+4
                                           if (bin_ci(kk+1,1)>0|| bin_p(kk+1,1)~=1)
                                              count_inh = count_inh+1;
                                              if count_inh == 2
                                                  %% take the index kk
                                                  x1 = [kk kk];
                                                   zone_end_bin=kk;
                                                temp_mag=horzcat(temp_mag,GP_FR_mean(1,kk));

                                                zone_name_end=horzcat(num2str(zone_mark),' zone end',' bin ',num2str(kk));
                                                plot(x1,y,'color','k','Linewidth',1,'DisplayName', zone_name_end);
                                                text(x1(2)-1,y(2),num2str(zone_mark),'Fontsize',12);
                                                word_cnt_in=word_cnt_in+1;
                                                %temp_Result_in{fold_cnt,zone_mark}=[zone_start_bin zone_end_bin]; 
                                                temp_Result_in{word_cnt_in}=[zone_start_bin zone_end_bin];
                                                magnitude_zone{1,zone_mark}=temp_mag;
                                                area_zone{1,zone_mark}=sum(temp_mag);%*(zone_end_bin-zone_start_bin+1);
                                                std_zone{1,zone_mark}=std(temp_mag);
                                                skew_Zone{1,zone_mark} = skewness(temp_mag);
                                                mean_zone{1,zone_mark} =mean(temp_mag);
                                                  break
                                              end
                                           end
                                         end
                                          
                                    end
                                    end
                            end%%%end of 1st inhibition detection  
                         else
                                      disp('enter for late inhibition')%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                                      x1 = [k+1 k+1];                     
                                      zone_mark=zone_mark+1;
                                      zone_start_bin=k;
                                      zone_name_start=horzcat(num2str(zone_mark),' zone start', ' bin ',num2str(k));
                                      plot(x1,y,'color','r','Linewidth',1,'DisplayName', zone_name_start)
                                      text(x1(2)-1,y(2),num2str(zone_mark),'Fontsize',12) 
                             
                                    for kin=k+1:Time_limit-40                      
                                        if(bin_ci(kin,1)<0)&&(bin_ci(kin+1,1)<0)&&(kin<=Time_limit-40)
                                             disp('continue');
                                             temp_mag=horzcat(temp_mag,GP_FR_mean(1,kin));
                                             cnt_early=cnt_early+1;
                                        else
                                            x1 = [kin kin];
                                            zone_end_bin=kin;
                                            temp_mag=horzcat(temp_mag,GP_FR_mean(1,kin));

                                            zone_name_end=horzcat(num2str(zone_mark),' zone end',' bin ',num2str(kin));
                                            plot(x1,y,'color','k','Linewidth',1,'DisplayName', zone_name_end);
                                            text(x1(2)-1,y(2),num2str(zone_mark),'Fontsize',12);
                                            word_cnt_in=word_cnt_in+1;
                                            temp_Result_in{word_cnt_in}=[zone_start_bin zone_end_bin];
                                            magnitude_zone{1,zone_mark}=temp_mag;
                                            area_zone{1,zone_mark}=sum(temp_mag);%*(zone_end_bin-zone_start_bin+1);
                                            std_zone{1,zone_mark}=std(temp_mag);
                                            skew_Zone{1,zone_mark} = skewness(temp_mag);
                                            mean_zone{1,zone_mark} =mean(temp_mag);
                                            break;
                                        end
                                    end 
                                    break;
                                 end
                             end%%%%%%%%%%%%%%%%%%%%%%%%%%%555temp_Result_in
                         end 

                  %%%for increment of k based on length
                  if(cnt_early>1)
                      k=kk+1;
                  else
                      k=k+1;
                  end
            end
                           
                         


%      %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 
%         legend show
%         xlabel('TIME')
%         ylabel('FR')
%         caxis([0, 1]);
%         %myStr = sprintf('basalFR %s basalstd %s',num2str(basal_FR),num2str(basal_FR_std));
%         %title(sprintf('Graph of %s', xls_file));
%         %title(myStr);
% %         sub_dest_path=horzcat(dest_folder,folder_plot_name);
% %         mkdir(sub_dest_path)
% %         dest_path=strcat(sub_dest_path,'\',file_plot_name,'late.png');
% %         saveas(f,dest_path) ;
% dest_path=strcat(dest_folder,'\', num2str(file_plot_name),'late.png');
%         saveas(f,dest_path) ;


end




function [temp_Result_ex,temp_Result_in,area_zone]=zone_Demarkation(Time_limit,stimulation_Start,GP_FR_mean,bin_ci,bin_p,dest_folder,folder_plot_name,file_plot_name)

            
 f = figure('Position', get(0, 'Screensize'));
 X_data = 1:length(GP_FR_mean);
 %%y_data=ones(1,200);
 f=bar(X_data,GP_FR_mean)  ;
 set(f,'FaceColor','c');                       
 grid on
 grid minor             
 hold on
 y = ylim;

k=stimulation_Start+7;
%temp_k=k;
word_cnt_ex=0;
word_cnt_in=0;
zone_mark=0;
early_flag=0;
temp_Result_ex=[];
temp_Result_in=[];
magnitude_zone=[];
area_zone=[];

            while(k<=Time_limit-40) 
                 cnt_early=1;
                 temp_mag=[];
                  if((bin_p(k,1)==1)&(bin_p(k+1,1)==1))
                  %if(bin_ci(k,1)>0)&&(bin_ci(k+1,1)>0)%excitated start
                       %if(bin_ci(k,1)>4)&&(bin_ci(k+1,1)>4)%excitated start
                       if(bin_ci(k,1)>3)&&(bin_ci(k+1,1)>3)%excitated start with STN col
                              early_flag=1;
                              if(cnt_early==1)
                                  x1 = [k k];                     
                                  zone_mark=zone_mark+1;
                                  zone_start_bin=k;
                                  
                                  
                                  zone_name_start=horzcat(num2str(zone_mark),' zone start', ' bin ',num2str(k));
                                   plot(x1,y,'color','r','Linewidth',1,'DisplayName', zone_name_start)
                                   text(x1(2)-1,y(2),num2str(zone_mark),'Fontsize',12)   
                                  
                              end
                              for kk=k:Time_limit -40                      
                                    %if(bin_ci(kk,1)>0)&&(bin_ci(kk+1,1)>0)
                                    if((bin_ci(kk,1)>0)&&(bin_ci(kk+1,1)>0)&&(bin_p(kk,1)==1)&(bin_p(kk+1,1)==1)) &&(kk<=Time_limit-40)
                                    %if((bin_ci(kk,1)>0)&&(bin_ci(kk+1,1)>0)&&(bin_p(kk,1)==1)&(bin_p(kk+1,1)==1))
                                         disp('continue');
                                         temp_mag=horzcat(temp_mag,GP_FR_mean(1,kk));
                                         
                                         cnt_early=cnt_early+1;
                                    elseif ((bin_ci(kk+1,1)<0)&&(bin_ci(kk+2,1)<0)||(bin_p(kk+1,1)~=1)&(bin_p(kk+2,1)~=1))
                                    %elseif ((bin_ci(kk+1,1)<0)&&(bin_ci(kk+2,1)<0)||(bin_p(kk+1,1)~=1)&(bin_p(kk+2,1)~=1))
                                        x1 = [kk kk];
                                        zone_end_bin=kk;
                                        temp_mag=horzcat(temp_mag,GP_FR_mean(1,kk));
                                        
                                        zone_name_end=horzcat(num2str(zone_mark),' zone end',' bin ',num2str(kk));
                                        plot(x1,y,'color','k','Linewidth',1,'DisplayName', zone_name_end);
                                        text(x1(2)-1,y(2),num2str(zone_mark),'Fontsize',12);  
                                        %%temp_Result_ex{fold_cnt,zone_mark}=[zone_start_bin zone_end_bin]; 
                                        word_cnt_ex=word_cnt_ex+1;
                                        temp_Result_ex{1,word_cnt_ex}=[zone_start_bin zone_end_bin];    
                                        magnitude_zone{1,zone_mark}=temp_mag;
                                        area_zone{1,zone_mark}=sum(temp_mag);%*(zone_end_bin-zone_start_bin+1);
                                        break;
                                    end
                              end
                       else%%for inhibition
                           if((early_flag==1)&(bin_ci(k,1)<0)&&(bin_ci(k+1,1)<0))%inhibited start
                               early_flag=0;
                               if(cnt_early==1)
                                  x1 = [k k];                     
                                  zone_mark=zone_mark+1;
                                  zone_start_bin=k;
                                  zone_name_start=horzcat(num2str(zone_mark),' zone start', ' bin ',num2str(k));
                                  plot(x1,y,'color','r','Linewidth',1,'DisplayName', zone_name_start)
                                  text(x1(2)-1,y(2),num2str(zone_mark),'Fontsize',12)                                    
                              end
                              for kk=k+1:Time_limit-40                      
                                    if(bin_ci(kk,1)<0)&&(bin_ci(kk+1,1)<0)&&(kk<=Time_limit-40)
                                         disp('continue');
                                         temp_mag=horzcat(temp_mag,GP_FR_mean(1,kk));
                                         cnt_early=cnt_early+1;
                                    else
                                        x1 = [kk kk];
                                        zone_end_bin=kk;
                                        temp_mag=horzcat(temp_mag,GP_FR_mean(1,kk));
                                        
                                        zone_name_end=horzcat(num2str(zone_mark),' zone end',' bin ',num2str(kk));
                                        plot(x1,y,'color','k','Linewidth',1,'DisplayName', zone_name_end);
                                        text(x1(2)-1,y(2),num2str(zone_mark),'Fontsize',12);
                                        word_cnt_in=word_cnt_in+1;
                                        %%temp_Result_in{fold_cnt,zone_mark}=[zone_start_bin zone_end_bin]; 
                                        temp_Result_in{1,word_cnt_in}=[zone_start_bin zone_end_bin];
                                        magnitude_zone{1,zone_mark}=temp_mag;
                                        area_zone{1,zone_mark}=sum(temp_mag);%*(zone_end_bin-zone_start_bin+1);
                                        break;
                                    end
                              end  
                           end
                       end
                  end
                  %%%for increment of k based on length
                  if(cnt_early>1)
                      k=kk+1;
                  else
                      k=k+1;
                  end
            end
                           
                         


%      %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 
        legend show
        xlabel('TIME')
        ylabel('FR')
        caxis([0, 1]);
        %myStr = sprintf('basalFR %s basalstd %s',num2str(basal_FR),num2str(basal_FR_std));
        %title(sprintf('Graph of %s', xls_file));
        %title(myStr);
        sub_dest_path=horzcat(dest_folder,folder_plot_name);
        mkdir(sub_dest_path)
        dest_path=strcat(sub_dest_path,'\', file_plot_name,'.png');
        saveas(f,dest_path) ;


end


 

