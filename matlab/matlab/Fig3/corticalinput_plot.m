function corticalinput_plot()
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here





hold on;
for kk=1:3  
    grphindex=kk;
    if(kk==2)
      grphindex=5;
    end
    if(kk==3)
        grphindex=9;
    end
Aa=load('\normal100Trials\dop_10_0.8_MultiTrial_100_CORTEX_Volt_20_N=50percnt_30ms_30ms_30ms.csv');
%subplot(ax{grphindex})
%bar(Aa)
%plot(Aa)
%plot(Aa)
%plot(Aa(640:799),'k','Linewidth',2)
 xlabel_data = 640:799;
 xlabel_data = xlabel_data - 700;%xx_fixed(1);
 plot(xlabel_data,Aa(640:799),'k','Linewidth',2); 
 xlim([-60 100]); 


%             xTickLocations = [-60, -40, -20, 0 , 20, 40, 60, 80, 100, 120, 140, 160]%linspace(-40, 160, 7);
%             xlabell=-60+floor(xTickLocations);
%             set(gca,'XTick',xTickLocations,'XTickLabel', xlabell,'FontWeight','bold');
%             xlim([0 160]);
            
          first_point = round(Aa(640));
           yTickLocations =[];
           ylabell = [];
           v_max=max(Aa(1,640:799)); 

yTickLocations =[0 50 100];
ylabell = [0 50 100]
set(gca,'YTick',yTickLocations,'YTickLabel', ylabell,'FontWeight','bold');           
%ylim([0 (v_max+30) ]) 
            
set(gca,'FontSize',14,'FontWeight','bold')

xlabel('Time (in ms)');
ylabel('mean FR (in Hz)');
%axis tight
box on

end
set(gcf,'Color',[1 1 1]);

saveas(gca,'fig3_cortical_input.png')


end

