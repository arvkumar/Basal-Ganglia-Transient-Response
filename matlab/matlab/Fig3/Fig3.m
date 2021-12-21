function Fig3()

 

source_Folder_single_Normal='\Fig3\normal100Trials\';
folders_normal=dir(horzcat(source_Folder_single_Normal,'\*MultiTrial*'));

source_Folder_single_TPD='\Fig3\PDTrip100Trials\';
folders_tpd =dir(horzcat(source_Folder_single_TPD,'\*MultiTrial*'));

source_Folder_single_BIP='\Fig3\AprilPDBip100Trials\';
folders_bip=dir(horzcat(source_Folder_single_BIP,'\*MultiTrial*'));



source_Folder_single_Normal_STN='\StnonlyStimulation_PDBiptripNormalFigure3\Norm_100Trials\';
folders_normal_STN=dir(horzcat(source_Folder_single_Normal_STN,'\*MultiTrial*'));

source_Folder_single_TPD_STN='\StnonlyStimulation_PDBiptripNormalFigure3\PDTrip\';
folders_tpd_STN =dir(horzcat(source_Folder_single_TPD_STN,'\*MultiTrial*'));

source_Folder_single_BIP_STN='\StnonlyStimulation_PDBiptripNormalFigure3\PDBip\';
folders_bip_STN=dir(horzcat(source_Folder_single_BIP_STN,'\*MultiTrial*'));



nuclei_name={'GPe-TA','GPe-TI','STN','SNr'};
color_code={'#E3B622', '#FFBF00','#DB741D', '#E51400'};% #0000ff

xx_fixed = [700 700];   
grphindex=0;

NType = [];
  for fileType=1:3
    if(fileType==1)
        source_Folder_single= source_Folder_single_Normal;
        folders=folders_normal;
        
        source_Folder_single_STN= source_Folder_single_Normal_STN;
        folders_en=folders_normal_STN;
        NType = 'in Normal condition';

    elseif(fileType==2)
         
         source_Folder_single= source_Folder_single_BIP;
         folders=folders_bip; 
         
         source_Folder_single_STN= source_Folder_single_BIP_STN;
         folders_en=folders_bip_STN;     
         NType = 'in PD-biphasic condition';
         
    else 
         source_Folder_single= source_Folder_single_TPD;
         folders=folders_tpd; 
         
         source_Folder_single_STN= source_Folder_single_TPD_STN;
         folders_en=folders_tpd_STN;
         NType = 'in PD-triphasic condition';
     end
   
    file_cnt=0;
for i = 1:4%N    
        figure;
		 grphindex=grphindex+1;
            %subplot(ax{grphindex})


             file_cnt=file_cnt+1;
            files_name= horzcat(source_Folder_single,folders(i).name)
            [v,T,vT]=xlsread(files_name) ; 
            first_point = round(v(640));
            
            %STN stimulation
            files_name_STN= horzcat(source_Folder_single_STN,folders_en(i).name)
            [v_STN,T_STN,vT_STN]=xlsread(files_name_STN) ; 

            %%b_STN =v_STN(40:199);%old data
            %b_STN =v_STN(640:799);

           str=color_code{i};
           colorplot = sscanf(str(2:end),'%2x%2x%2x',[1 3])/255;
           %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%FSI%%%%%%%%%%%
%             if(i==3)
%            yTickLocations =[];
%            ylabell = [];
%            v_max=max(v(1,640:799)); 
%            plot (v(1,640:799),'Color',colorplot,'LineWidth',1.5) 
%            %xlabel_data = 640:799;
%            %xlabel_data = xlabel_data - xx_fixed(1);
%            %plot(xlabel_data,v(1,640:799),'color', colorplot,'Linewidth',1.5);
%            
%            gg_index =1 ;
%                    while (gg_index <= v_max+10)
%                     yTickLocations (gg_index) = first_point*(gg_index-1);            
%                     ylabell (gg_index) =floor(yTickLocations (gg_index));
%                     gg_index = gg_index+1;
%                    end
%                 set(gca,'YTick',yTickLocations,'YTickLabel', ylabell,'FontWeight','bold');           
%                 ylim([-1 (v_max+first_point) ]) 
%             end  
           
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%TA_SNR%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%           
           if(fileType ==2  & i==3)%%STN
             %plot ((v(1,640:799)-10),'Color',colorplot,'LineWidth',1.5)
             %v_e=v(1,640:799)-10;
             xlabel_data = 640:799;
             xlabel_data = xlabel_data - 700;%xx_fixed(1);
	         plot(xlabel_data,v(1,640:799)-10,'color', colorplot,'Linewidth',1.5);  
             xlim([-60 100]);
           else
             xlabel_data = 640:799;
             xlabel_data = xlabel_data - 700;%xx_fixed(1);
	         plot(xlabel_data,v(1,640:799),'color', colorplot,'Linewidth',1.5);   
             xlim([-60 100]); 
            %plot (v(1,640:799),'Color',colorplot,'LineWidth',1.5)   
           end

            v_max=max(v(1,640:799)); 
           if (fileType ==2  & i==3)
            %set(gca,'YTick',[0 30 60],'YTickLabel', [0 30 60],'FontWeight','bold'); 
            set(gca,'YTick',[0 20 40 60],'YTickLabel', [0 30 60 90],'FontWeight','bold');       
            ylim([10 60]) 
            
           else if  (fileType ==3 & i==3)
            set(gca,'YTick',[0 30 60 90 120 150],'YTickLabel', [0 30 60 90 120 150],'FontWeight','bold');           
            ylim([-1 (v_max+first_point) ]) 
               else
                   gg_index =1 ;
                   while (gg_index <= v_max+10)
                    yTickLocations (gg_index) = first_point*(gg_index-1); 
                    %yTickLocations (2) = first_point*1; 
                    %yTickLocations (3) = first_point*2;           
                    ylabell (gg_index) =floor(yTickLocations (gg_index));
                    %ylabell (2) =first_point+floor(yTickLocations (1)); 
                    %ylabell (3) =first_point+floor(yTickLocations (2));  
                    gg_index = gg_index+1;
                   end
                set(gca,'YTick',yTickLocations,'YTickLabel', ylabell,'FontWeight','bold');           
                ylim([-1 (v_max+first_point) ]) 
               end
            end                   
            if (i==4)||(i==1)||(i==2)%(i>4)%(i==4)||(i==1)||(i==2)
            hold on;
            %plot (b_STN,'g','LineWidth',1)
             xlabel_data = 640:799;
             xlabel_data = xlabel_data - 700;%xx_fixed(1);
	         plot(xlabel_data,v_STN(640:799),'g','Linewidth',1.5); 
             xlim([-60 100]); 
            end
            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
            
            
% %             xTickLocations = linspace(1, 160, 5);
% %             xlabell=-60+floor(xTickLocations);

%             xTickLocations = [-60, -40, -20, 0 , 20, 40, 60, 80, 100, 120, 140, 160]%linspace(-40, 160, 7);
%             xlabell=-60+floor(xTickLocations);
%             set(gca,'XTick',xTickLocations,'XTickLabel', xlabell,'FontWeight','bold');
%             xlim([0 160]);
            title(horzcat(nuclei_name{i},' ',NType));
            
            

            
            

            %if(fileType==1)
            ylabel('mean FR (in Hz)');
            %%legend  show
            %end
            %if(i==4)
            xlabel('Time (in ms)');
%             %line([60,60], ylim, 'Color', 'k', 'LineWidth', 1); % Draw line for Y axis.
%             %ylim([-1 200]) 
            %end
            line([700-xx_fixed(1),700-xx_fixed(1)], ylim, 'Color', 'k', 'LineWidth', 1); % Draw line for Y axis.
            hold on;
           set(gca,'FontSize',14,'FontWeight','bold')
end

end

set(gcf, 'InvertHardCopy', 'off');
set(gcf,'Color',[1 1 1]); 
set(gca,'FontSize',14,'FontWeight','bold')
%set(gca,'defaultAxesFontSize',11,FontWeight','bold')
%set(findall(gcf,'-property','FontSize'),'FontSize',11)  

saveas(gca,'april16data_fig3.png')

end

