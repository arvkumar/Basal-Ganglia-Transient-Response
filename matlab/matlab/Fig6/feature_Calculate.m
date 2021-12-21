function feature_Calculate(source_folder,third_zone_Data,magnitude_file,zone_file_name,std_file,mean_file,max_min_Zone,basal_FR_zone_array,file_name_disconnection,stimulation_point,output_file1,output_file2,num)
%UNTITLED4 Summary of this function goes here
%   Detailed explanation goes here
mkdir(source_folder);
file_name_magnitude=magnitude_file;%load(magnitude_file);%load(horzcat(source_folder_name,'result_sum_magnitude_test.txt'));
%zone_Data=zone_file_name;%load(zone_file_name);
updated_Zone_rel_d=zone_file_name;
dop_level=5;
zone_till=4;

fp=fopen(file_name_disconnection,'r');
cnt_line=1;
file_mat=[];

tline = fgetl(fp);
file_mat{1,1}=tline;
while ischar(tline)
    cnt_line=cnt_line+1;
    %disp(tline)
    tline = fgetl(fp);
    rest=tline;   
	%cnt_word=0;
    %while(length(rest)~=0)
    %    cnt_word=cnt_word+1;
    %[num, ~] =strtok(rest,'.csv');
     file_mat{cnt_line,1}=rest;
    %end
end
fclose(fp);
file_mat=file_mat';
dest_file=horzcat(source_folder,output_file2);
%save(dest_file,'updated_Zone_rel_d','-ascii');
data=updated_Zone_rel_d;
                             
                %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                 source_folder_name=horzcat(source_folder,'zone4_allwithoutnorm_basal_cv\');
                 data_mat=[];
                 mkdir(source_folder_name)
                % data_mat=horzcat(data,file_name_magnitude,mean_file,std_file,max_min_Zone,inhibition_Area);  
                data_mat=horzcat(data,file_name_magnitude,mean_file,std_file,max_min_Zone);
                [data_mat, Dist_normal_table]=dist_Combination_without_normal(data_mat);                                  
                [Dist_normal,Dist_PD,ref_Data,ref_file_mat]=estimate_normal_PD(data_mat);
                %bb=[close_normal,close_PD];
                %xlswrite(dest_file, bb, 'zone4_allwithoutnorm_basavl_CV')
                source_folder_name=[];
                 [close_normal,close_PD,norm_pd_rank,pd_norm_rank,index_close_normal,index_close_PD]=paretorank_visualize(Dist_normal,Dist_PD,file_mat,source_folder_name,num);
              
end

function [close_normal,close_PD,norm_pd_rank,pd_norm_rank,index_close_normal,index_close_PD]=paretorank_visualize(Dist_normal,Dist_PD,ref_file_mat,source_folder_name,num)

norm_pd_rank=0;
pd_norm_rank=0;
                ref_file_mat=ref_file_mat';
                [val_normal index_close_normal]=sort(Dist_normal); %minimum will be closer to normal

                  for i=1:size(index_close_normal,1)
                      close_normal{i,:}=horzcat(ref_file_mat{index_close_normal(i),1},' ',num2str(val_normal(i,1))) ;   
                  end
                % 
                  dest_file1=horzcat( source_folder_name,'\','method',num2str(num),'close_normal.txt');
                %  %save(dest_file1,close_normal,'-ascii')
                  filePh = fopen(dest_file1,'w');
                 fprintf(filePh,'%s\n',close_normal{:});
                 fclose(filePh);

                %%close to PD

                [val_close_PD index_close_PD]=sort(Dist_PD); %minimum will be closer to PD

                  for i=1:size(index_close_PD,1)
                      close_PD{i,:}=horzcat(ref_file_mat{index_close_PD(i),1},' ',num2str(val_close_PD(i,1))) ;   
                  end

                dest_file2=horzcat( source_folder_name,'\','method',num2str(num2str(num)),'close_PD.txt');
                %save(dest_file1,close_normal,'-ascii')
                filePh = fopen(dest_file2,'w');
                fprintf(filePh,'%s\n',close_PD{:});
                fclose(filePh); 
                %ref_file_mat={'D1-SNr', 'D2-TI', 'STN-TI Loop', 'TA-TI laterals'};
                %ref_file_mat={'D2-TI', 'TA-TI collaterals','STN-TI
                %Loop','D1-SNr'};old paper
                
                ref_file_mat={'D2-TI','TA-TI collaterals','STN-TI Loop','D1-SNr'};
                ref_file_mat=ref_file_mat';
                xlabel=ref_file_mat;

                PD_distance_based_on_normal=Dist_PD(index_close_normal);

                               
                val_normal_temp(1,1)=val_normal(2,1);
                val_normal_temp(2,1)=val_normal(3,1);
                val_normal_temp(3,1)=val_normal(4,1);
                val_normal_temp(4,1)=val_normal(6,1);
                
                PD_distance_based_on_normal_temp(1,1)=PD_distance_based_on_normal(2,1);
                PD_distance_based_on_normal_temp(2,1)=PD_distance_based_on_normal(3,1);
                PD_distance_based_on_normal_temp(3,1)=PD_distance_based_on_normal(4,1);                
                PD_distance_based_on_normal_temp(4,1)=PD_distance_based_on_normal(6,1);
                
                
                grouped_dummy=[val_normal_temp PD_distance_based_on_normal_temp];

                grouped=grouped_dummy;
                 h=bar(grouped);
                 %h=bar((1:2:8),grouped);                 
                % color_code={'#00876c','#de0000' };%or 
                 color_code={'#64c98a','#de0000'};
                 
                str = color_code{1};%'#87EBB1';%#FF0000';
                color = sscanf(str(2:end),'%2x%2x%2x',[1 3])/255;
                h(1).FaceColor = color;

                str = color_code{2};%'#CE0241';%#FF0000';
                color = sscanf(str(2:end),'%2x%2x%2x',[1 3])/255;
                h(2).FaceColor = color;
                str = '#EAEAEA';%#FF0000';
                bgcolor = sscanf(str(2:end),'%2x%2x%2x',[1 3])/255;
                %set(gca,'Color',bgcolor)
                
                xTickLocations = linspace(1, 4, 4);
                %set(gca,'Color',[1, 0.8, 0.9])
                %ylim([1 max(max(grouped))+0.2]);
                set(gca,'XTick',xTickLocations,'XTickLabel', xlabel,'FontWeight','bold');
                legend('From normal condition','From PD condition','Position','north')
                % lgd=legend('Normalized Distance from Normal','Normalized Distance from PD','Position',[0.4637 0.6075 0.4179 0.0869])
                ylabel('Distance')
                set(gca,'Color',[1 1 1]);
                %str= horzcat('Significant Synaptic Weight (for Control Group)')
                %title(str);
                saveas(gca,'Figure6.png') ;
                close all;

                              
end


function [Dist_normal,Dist_PD,refined_data,file_ref]=estimate_normal_PD(data);

name_file=0;
file_ref=[];

%data_mat=horzcat(data,file_name_magnitude_norm);
data_mat=data;%horzcat(data,file_name_magnitude_norm);

refined_data=data_mat;
%file_ref=file_mat;
normal=refined_data(1,:);
PD=refined_data(2,:);
 for k=1: size(refined_data,1)
        test_Vec=refined_data(k,:);
        Dist_normal(k,1) = sqrt(sum(normal-test_Vec).^2);%pdist2(normal,test_Vec,'euclidean');
        Dist_PD(k,1) = sqrt(sum(PD-test_Vec).^2); %pdist2(PD,test_Vec,'euclidean');   
 end
  %dest_file=horzcat( source_folder_name,'zone',num2str(zone_till),'dist.txt');
  %dest_file=horzcat( source_folder_name,'dist_withnormarea_pareto_bargraph.xlsx');
  %save(dest_file,'Dist_normal','-ascii')
  %xlswrite(dest_file,Dist_normal);
end





function [data_mat,Dist_normal]=dist_Combination_without_normal(data_mat)
for k=1: size(data_mat,1)
    %check_data=data_mat(k,1:2*zone_till);
    check_data=data_mat(k,:);
    for i=1:size(data_mat,1)
        %vec2=data_mat(i,1:2*zone_till);
        vec2=data_mat(i,:);
        Dist_normal(i,k) = pdist2(check_data,vec2,'euclidean');
        %Dist_PD(i,k) = pdist2(vec1_PD,vec2,'euclidean');   
    end
 end
  %dest_file=horzcat( source_folder_name,'zone',num2str(zone_till),'dist.txt');
  %dest_file=horzcat( source_folder_name,output_file);
  %save(dest_file,'Dist_normal','-ascii')
  %xlswrite(dest_file,Dist_normal);
end







