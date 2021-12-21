function Fig5_heatmap()
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
close all;
 A=load('duration.txt');
 B=load('area.txt');

AA_dur=A(:,2:2:8);
BB_area=abs(B);

normal_row =[7.0000    4.0000   11.0000    6.0000   17.0000    9.3000   26.3000   10.6100];
normal_Area =[258.3304   36.1512  710.2501  276.4640];

normal_row_duraion=normal_row(1,2:2:8);
A_dur=[];
B_area=[];
A_dur=[AA_dur ;normal_row_duraion];
B_area=[BB_area ;normal_Area];

norm_Data_A_duration=A_dur;
norm_data_B_Area=B_area;


singleLoop=cell(12,1);
%hfig = figure('Position', get(0, 'Screensize'));
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
connectionName{1,1}='D1-SNr';
decreasedDataDuration_temp=norm_Data_A_duration(1:1+2,:);
decreasedDataDuration=flipud(decreasedDataDuration_temp);
increaseDataDuration=norm_Data_A_duration(4:4+2,:);
plotNum1=1;

normalDuration=norm_Data_A_duration(37,:);
normalArea=norm_data_B_Area(37,:);

decreasedDataArea_temp=norm_data_B_Area(1:1+2,:);
decreasedDataArea=flipud(decreasedDataArea_temp);
increaseDataArea=norm_data_B_Area(4:4+2,:);
plotNum2=7;


data_zone1_duration=[decreasedDataDuration(:,1);normalDuration(1,1);increaseDataDuration(:,1)];
data_zone2_duration=[decreasedDataDuration(:,2);normalDuration(1,2);increaseDataDuration(:,2)];
data_zone3_duration=[decreasedDataDuration(:,3);normalDuration(1,3);increaseDataDuration(:,3)];
data_zone4_duration=[decreasedDataDuration(:,4);normalDuration(1,4);increaseDataDuration(:,4)];

data_zone_duration{1,:}=[data_zone1_duration';data_zone2_duration';data_zone3_duration';data_zone4_duration'];

data_zone1_norm_dd=data_zone1_duration./data_zone1_duration(4,1);%
data_zone2_norm_dd=data_zone2_duration./data_zone2_duration(4,1);%
data_zone3_norm_dd=data_zone3_duration./data_zone3_duration(4,1);
data_zone4_norm_dd=data_zone4_duration./data_zone4_duration(4,1);
singleLoop{1,1}=[data_zone1_norm_dd';data_zone2_norm_dd';data_zone3_norm_dd';data_zone4_norm_dd'];


%singleLoop{1,1}=[data_zone1_duration';data_zone2_duration';data_zone3_duration';data_zone4_duration'];

data_zone1_area=[decreasedDataArea(:,1);normalArea(1,1);increaseDataArea(:,1)];
data_zone2_area=[decreasedDataArea(:,2);normalArea(1,2);increaseDataArea(:,2)];
data_zone3_area=[decreasedDataArea(:,3);normalArea(1,3);increaseDataArea(:,3)];
data_zone4_area=[decreasedDataArea(:,4);normalArea(1,4);increaseDataArea(:,4)];


data_zone1_norm=data_zone1_area./data_zone1_duration;%(data_zone1 - (min(data_zone1))) / ( (max(data_zone1)) - (min(data_zone1)) );
%data_zone1_norm_nn=data_zone1_norm./data_zone1_norm(4,1);%

data_zone2_norm=data_zone2_area./data_zone2_duration;%(data_zone2 - (min(data_zone2))) / ( (max(data_zone2)) - (min(data_zone2)) );
%data_zone2_norm_nn=data_zone2_norm./data_zone2_norm(4,1);%

data_zone3_norm=data_zone3_area./data_zone3_duration;%(data_zone3 - (min(data_zone3))) / ( (max(data_zone3)) - (min(data_zone3)) );
%data_zone3_norm_nn=data_zone3_norm./data_zone3_norm(4,1);

data_zone4_norm=data_zone4_area./data_zone4_duration;%(data_zone4 - (min(data_zone4))) / ( (max(data_zone4)) - (min(data_zone4)) );
%data_zone4_norm_nn=data_zone4_norm./data_zone4_norm(4,1);


data_zone1_norm_nn=data_zone1_norm./data_zone1_norm(4,1);%
data_zone2_norm_nn=data_zone2_norm./data_zone2_norm(4,1);%
data_zone3_norm_nn=data_zone3_norm./data_zone3_norm(4,1);
data_zone4_norm_nn=data_zone4_norm./data_zone4_norm(4,1);
singleLoop{7,1}=[data_zone1_norm_nn';data_zone2_norm_nn';data_zone3_norm_nn';data_zone4_norm_nn'];
%data_zone_area{1,:}=[data_zone1_norm';data_zone2_norm';data_zone3_norm';data_zone4_norm'];
%singleLoop{7,1}=[data_zone1_norm';data_zone2_norm';data_zone3_norm';data_zone4_norm'];
%singleLoop{7,1}=[data_zone1_norm_nn';data_zone2_norm_nn';data_zone3_norm_nn';data_zone4_norm_nn'];

%subplot_visualize(hfig,decreasedDataDuration,normalDuration,increaseDataDuration,decreasedDataArea,normalArea,increaseDataArea,plotNum1,plotNum2,connectionName);
%subplot_density_visualize(hfig,decreasedDataDuration,normalDuration,increaseDataDuration,decreasedDataArea,normalArea,increaseDataArea,plotNum1,plotNum2,connectionName);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
decreasedDataArea=[];;increaseDataArea=[];decreasedDataDuration=[];increaseDataDuration=[];
data_zone1_duration=[];data_zone2_duration=[];data_zone3_duration=[];data_zone4_duration=[];
data_zone1_area=[];data_zone2_area=[];data_zone3_area=[];data_zone4_area=[];
data_zone1_norm=[];data_zone2_norm=[];data_zone3_norm=[];data_zone4_norm=[];
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

connectionName{2,1}='D2-TI';
decreasedDataDuration_temp=norm_Data_A_duration(7:7+2,:);
decreasedDataDuration=flipud(decreasedDataDuration_temp);
increaseDataDuration=norm_Data_A_duration(10:10+2,:);
plotNum1=2;

decreasedDataArea_temp=norm_data_B_Area(7:7+2,:);
decreasedDataArea=flipud(decreasedDataArea_temp);
increaseDataArea=norm_data_B_Area(10:10+2,:);
plotNum2=8;


data_zone1_duration=[decreasedDataDuration(:,1);normalDuration(1,1);increaseDataDuration(:,1)];
data_zone2_duration=[decreasedDataDuration(:,2);normalDuration(1,2);increaseDataDuration(:,2)];
data_zone3_duration=[decreasedDataDuration(:,3);normalDuration(1,3);increaseDataDuration(:,3)];
data_zone4_duration=[decreasedDataDuration(:,4);normalDuration(1,4);increaseDataDuration(:,4)];

data_zone_duration{2,:}=[data_zone1_duration';data_zone2_duration';data_zone3_duration';data_zone4_duration'];

data_zone1_norm_dd=data_zone1_duration./data_zone1_duration(4,1);%
data_zone2_norm_dd=data_zone2_duration./data_zone2_duration(4,1);%
data_zone3_norm_dd=data_zone3_duration./data_zone3_duration(4,1);
data_zone4_norm_dd=data_zone4_duration./data_zone4_duration(4,1);
singleLoop{2,1}=[data_zone1_norm_dd';data_zone2_norm_dd';data_zone3_norm_dd';data_zone4_norm_dd'];

%singleLoop{2,1}=[data_zone1_duration';data_zone2_duration';data_zone3_duration';data_zone4_duration'];

data_zone1_area=[decreasedDataArea(:,1);normalArea(1,1);increaseDataArea(:,1)];
data_zone2_area=[decreasedDataArea(:,2);normalArea(1,2);increaseDataArea(:,2)];
data_zone3_area=[decreasedDataArea(:,3);normalArea(1,3);increaseDataArea(:,3)];
data_zone4_area=[decreasedDataArea(:,4);normalArea(1,4);increaseDataArea(:,4)];


data_zone1_norm=data_zone1_area./data_zone1_duration;%(data_zone1 - (min(data_zone1))) / ( (max(data_zone1)) - (min(data_zone1)) );
data_zone2_norm=data_zone2_area./data_zone2_duration;%(data_zone2 - (min(data_zone2))) / ( (max(data_zone2)) - (min(data_zone2)) );
data_zone3_norm=data_zone3_area./data_zone3_duration;%(data_zone3 - (min(data_zone3))) / ( (max(data_zone3)) - (min(data_zone3)) );
data_zone4_norm=data_zone4_area./data_zone4_duration;%(data_zone4 - (min(data_zone4))) / ( (max(data_zone4)) - (min(data_zone4)) );


data_zone1_norm_nn=data_zone1_norm./data_zone1_norm(4,1);%
data_zone2_norm_nn=data_zone2_norm./data_zone2_norm(4,1);%
data_zone3_norm_nn=data_zone3_norm./data_zone3_norm(4,1);
data_zone4_norm_nn=data_zone4_norm./data_zone4_norm(4,1);
singleLoop{8,1}=[data_zone1_norm_nn';data_zone2_norm_nn';data_zone3_norm_nn';data_zone4_norm_nn'];


data_zone_area{2,:}=[data_zone1_norm';data_zone2_norm';data_zone3_norm';data_zone4_norm'];
%singleLoop{8,1}=[data_zone1_norm';data_zone2_norm';data_zone3_norm';data_zone4_norm'];



%subplot_visualize(hfig,decreasedDataDuration,normalDuration,increaseDataDuration,decreasedDataArea,normalArea,increaseDataArea,plotNum1,plotNum2,connectionName);
%subplot_density_visualize(hfig,decreasedDataDuration,normalDuration,increaseDataDuration,decreasedDataArea,normalArea,increaseDataArea,plotNum1,plotNum2,connectionName);

disp('end')
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
decreasedDataArea=[];increaseDataArea=[];decreasedDataDuration=[];increaseDataDuration=[];
data_zone1_duration=[];data_zone2_duration=[];data_zone3_duration=[];data_zone4_duration=[];
data_zone1_area=[];data_zone2_area=[];data_zone3_area=[];data_zone4_area=[];
data_zone1_norm=[];data_zone2_norm=[];data_zone3_norm=[];data_zone4_norm=[];
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
connectionName{3,1}='TA-TI';
decreasedDataDuration_temp=norm_Data_A_duration(13:13+2,:);
decreasedDataDuration=flipud(decreasedDataDuration_temp);
increaseDataDuration=norm_Data_A_duration(16:16+2,:);
plotNum1=3;

decreasedDataArea_temp=norm_data_B_Area(13:13+2,:);
decreasedDataArea=flipud(decreasedDataArea_temp);
increaseDataArea=norm_data_B_Area(16:16+2,:);
plotNum2=9;

data_zone1_duration=[decreasedDataDuration(:,1);normalDuration(1,1);increaseDataDuration(:,1)];
data_zone2_duration=[decreasedDataDuration(:,2);normalDuration(1,2);increaseDataDuration(:,2)];
data_zone3_duration=[decreasedDataDuration(:,3);normalDuration(1,3);increaseDataDuration(:,3)];
data_zone4_duration=[decreasedDataDuration(:,4);normalDuration(1,4);increaseDataDuration(:,4)];

data_zone_duration{3,:}=[data_zone1_duration';data_zone2_duration';data_zone3_duration';data_zone4_duration'];
data_zone1_norm_dd=data_zone1_duration./data_zone1_duration(4,1);%
data_zone2_norm_dd=data_zone2_duration./data_zone2_duration(4,1);%
data_zone3_norm_dd=data_zone3_duration./data_zone3_duration(4,1);
data_zone4_norm_dd=data_zone4_duration./data_zone4_duration(4,1);
singleLoop{3,1}=[data_zone1_norm_dd';data_zone2_norm_dd';data_zone3_norm_dd';data_zone4_norm_dd'];
%singleLoop{3,1}=[data_zone1_duration';data_zone2_duration';data_zone3_duration';data_zone4_duration'];

data_zone1_area=[decreasedDataArea(:,1);normalArea(1,1);increaseDataArea(:,1)];
data_zone2_area=[decreasedDataArea(:,2);normalArea(1,2);increaseDataArea(:,2)];
data_zone3_area=[decreasedDataArea(:,3);normalArea(1,3);increaseDataArea(:,3)];
data_zone4_area=[decreasedDataArea(:,4);normalArea(1,4);increaseDataArea(:,4)];


data_zone1_norm=data_zone1_area./data_zone1_duration;%(data_zone1 - (min(data_zone1))) / ( (max(data_zone1)) - (min(data_zone1)) );
data_zone2_norm=data_zone2_area./data_zone2_duration;%(data_zone2 - (min(data_zone2))) / ( (max(data_zone2)) - (min(data_zone2)) );
data_zone3_norm=data_zone3_area./data_zone3_duration;%(data_zone3 - (min(data_zone3))) / ( (max(data_zone3)) - (min(data_zone3)) );
data_zone4_norm=data_zone4_area./data_zone4_duration;%(data_zone4 - (min(data_zone4))) / ( (max(data_zone4)) - (min(data_zone4)) );

data_zone1_norm_nn=data_zone1_norm./data_zone1_norm(4,1);%
data_zone2_norm_nn=data_zone2_norm./data_zone2_norm(4,1);%
data_zone3_norm_nn=data_zone3_norm./data_zone3_norm(4,1);
data_zone4_norm_nn=data_zone4_norm./data_zone4_norm(4,1);
singleLoop{9,1}=[data_zone1_norm_nn';data_zone2_norm_nn';data_zone3_norm_nn';data_zone4_norm_nn'];


data_zone_area{3,:}=[data_zone1_norm';data_zone2_norm';data_zone3_norm';data_zone4_norm'];
%singleLoop{9,1}=[data_zone1_norm';data_zone2_norm';data_zone3_norm';data_zone4_norm'];

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
decreasedDataArea=[];increaseDataArea=[];decreasedDataDuration=[];increaseDataDuration=[];
data_zone1_duration=[];data_zone2_duration=[];data_zone3_duration=[];data_zone4_duration=[];
data_zone1_area=[];data_zone2_area=[];data_zone3_area=[];data_zone4_area=[];
data_zone1_norm=[];data_zone2_norm=[];data_zone3_norm=[];data_zone4_norm=[];
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%subplot_visualize(hfig,decreasedDataDuration,normalDuration,increaseDataDuration,decreasedDataArea,normalArea,increaseDataArea,plotNum1,plotNum2,connectionName);
%subplot_density_visualize(hfig,decreasedDataDuration,normalDuration,increaseDataDuration,decreasedDataArea,normalArea,increaseDataArea,plotNum1,plotNum2,connectionName);

connectionName{4,1}='TI-TA';

decreasedDataDuration_temp=norm_Data_A_duration(19:19+2,:);
decreasedDataDuration=flipud(decreasedDataDuration_temp);
increaseDataDuration=norm_Data_A_duration(22:22+2,:);
plotNum1=4;

decreasedDataArea_temp=norm_data_B_Area(19:19+2,:);
decreasedDataArea=flipud(decreasedDataArea_temp);
increaseDataArea=norm_data_B_Area(22:22+2,:);
plotNum2=10;
%subplot_visualize(hfig,decreasedDataDuration,normalDuration,increaseDataDuration,decreasedDataArea,normalArea,increaseDataArea,plotNum1,plotNum2,connectionName);
%subplot_density_visualize(hfig,decreasedDataDuration,normalDuration,increaseDataDuration,decreasedDataArea,normalArea,increaseDataArea,plotNum1,plotNum2,connectionName);

data_zone1_duration=[decreasedDataDuration(:,1);normalDuration(1,1);increaseDataDuration(:,1)];
data_zone2_duration=[decreasedDataDuration(:,2);normalDuration(1,2);increaseDataDuration(:,2)];
data_zone3_duration=[decreasedDataDuration(:,3);normalDuration(1,3);increaseDataDuration(:,3)];
data_zone4_duration=[decreasedDataDuration(:,4);normalDuration(1,4);increaseDataDuration(:,4)];

data_zone_duration{4,:}=[data_zone1_duration';data_zone2_duration';data_zone3_duration';data_zone4_duration'];
%singleLoop{4,1}=[data_zone1_duration';data_zone2_duration';data_zone3_duration';data_zone4_duration'];

data_zone1_norm_dd=data_zone1_duration./data_zone1_duration(4,1);%
data_zone2_norm_dd=data_zone2_duration./data_zone2_duration(4,1);%
data_zone3_norm_dd=data_zone3_duration./data_zone3_duration(4,1);
data_zone4_norm_dd=data_zone4_duration./data_zone4_duration(4,1);
singleLoop{4,1}=[data_zone1_norm_dd';data_zone2_norm_dd';data_zone3_norm_dd';data_zone4_norm_dd'];

data_zone1_area=[decreasedDataArea(:,1);normalArea(1,1);increaseDataArea(:,1)];
data_zone2_area=[decreasedDataArea(:,2);normalArea(1,2);increaseDataArea(:,2)];
data_zone3_area=[decreasedDataArea(:,3);normalArea(1,3);increaseDataArea(:,3)];
data_zone4_area=[decreasedDataArea(:,4);normalArea(1,4);increaseDataArea(:,4)];


data_zone1_norm=data_zone1_area./data_zone1_duration;%(data_zone1 - (min(data_zone1))) / ( (max(data_zone1)) - (min(data_zone1)) );
data_zone2_norm=data_zone2_area./data_zone2_duration;%(data_zone2 - (min(data_zone2))) / ( (max(data_zone2)) - (min(data_zone2)) );
data_zone3_norm=data_zone3_area./data_zone3_duration;%(data_zone3 - (min(data_zone3))) / ( (max(data_zone3)) - (min(data_zone3)) );
data_zone4_norm=data_zone4_area./data_zone4_duration;%(data_zone4 - (min(data_zone4))) / ( (max(data_zone4)) - (min(data_zone4)) );


data_zone_area{4,:}=[data_zone1_norm';data_zone2_norm';data_zone3_norm';data_zone4_norm'];
%singleLoop{10,1}=[data_zone1_norm';data_zone2_norm';data_zone3_norm';data_zone4_norm'];

data_zone1_norm_nn=data_zone1_norm./data_zone1_norm(4,1);%
data_zone2_norm_nn=data_zone2_norm./data_zone2_norm(4,1);%
data_zone3_norm_nn=data_zone3_norm./data_zone3_norm(4,1);
data_zone4_norm_nn=data_zone4_norm./data_zone4_norm(4,1);
singleLoop{10,1}=[data_zone1_norm_nn';data_zone2_norm_nn';data_zone3_norm_nn';data_zone4_norm_nn'];


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
decreasedDataArea=[];increaseDataArea=[];decreasedDataDuration=[];increaseDataDuration=[];
data_zone1_duration=[];data_zone2_duration=[];data_zone3_duration=[];data_zone4_duration=[];
data_zone1_area=[];data_zone2_area=[];data_zone3_area=[];data_zone4_area=[];
data_zone1_norm=[];data_zone2_norm=[];data_zone3_norm=[];data_zone4_norm=[];
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
connectionName{5,1}='STN-TI';
decreasedDataDuration_temp=norm_Data_A_duration(25:25+2,:);
decreasedDataDuration=flipud(decreasedDataDuration_temp);
increaseDataDuration=norm_Data_A_duration(28:28+2,:);
plotNum1=5;
 
decreasedDataArea_temp=norm_data_B_Area(25:25+2,:);
decreasedDataArea=flipud(decreasedDataArea_temp);
increaseDataArea=norm_data_B_Area(28:28+2,:);
plotNum2=11;

data_zone1_duration=[decreasedDataDuration(:,1);normalDuration(1,1);increaseDataDuration(:,1)];
data_zone2_duration=[decreasedDataDuration(:,2);normalDuration(1,2);increaseDataDuration(:,2)];
data_zone3_duration=[decreasedDataDuration(:,3);normalDuration(1,3);increaseDataDuration(:,3)];
data_zone4_duration=[decreasedDataDuration(:,4);normalDuration(1,4);increaseDataDuration(:,4)];

data_zone_duration{5,:}=[data_zone1_duration';data_zone2_duration';data_zone3_duration';data_zone4_duration'];
%singleLoop{5,1}=[data_zone1_duration';data_zone2_duration';data_zone3_duration';data_zone4_duration'];
data_zone1_norm_dd=data_zone1_duration./data_zone1_duration(4,1);%
data_zone2_norm_dd=data_zone2_duration./data_zone2_duration(4,1);%
data_zone3_norm_dd=data_zone3_duration./data_zone3_duration(4,1);
data_zone4_norm_dd=data_zone4_duration./data_zone4_duration(4,1);
singleLoop{5,1}=[data_zone1_norm_dd';data_zone2_norm_dd';data_zone3_norm_dd';data_zone4_norm_dd'];

data_zone1_area=[decreasedDataArea(:,1);normalArea(1,1);increaseDataArea(:,1)];
data_zone2_area=[decreasedDataArea(:,2);normalArea(1,2);increaseDataArea(:,2)];
data_zone3_area=[decreasedDataArea(:,3);normalArea(1,3);increaseDataArea(:,3)];
data_zone4_area=[decreasedDataArea(:,4);normalArea(1,4);increaseDataArea(:,4)];


data_zone1_norm=data_zone1_area./data_zone1_duration;%(data_zone1 - (min(data_zone1))) / ( (max(data_zone1)) - (min(data_zone1)) );
data_zone2_norm=data_zone2_area./data_zone2_duration;%(data_zone2 - (min(data_zone2))) / ( (max(data_zone2)) - (min(data_zone2)) );
data_zone3_norm=data_zone3_area./data_zone3_duration;%(data_zone3 - (min(data_zone3))) / ( (max(data_zone3)) - (min(data_zone3)) );
data_zone4_norm=data_zone4_area./data_zone4_duration;%(data_zone4 - (min(data_zone4))) / ( (max(data_zone4)) - (min(data_zone4)) );


data_zone_area{5,:}=[data_zone1_norm';data_zone2_norm';data_zone3_norm';data_zone4_norm'];
%singleLoop{11,1}=[data_zone1_norm';data_zone2_norm';data_zone3_norm';data_zone4_norm'];

data_zone1_norm_nn=data_zone1_norm./data_zone1_norm(4,1);%
data_zone2_norm_nn=data_zone2_norm./data_zone2_norm(4,1);%
data_zone3_norm_nn=data_zone3_norm./data_zone3_norm(4,1);
data_zone4_norm_nn=data_zone4_norm./data_zone4_norm(4,1);
singleLoop{11,1}=[data_zone1_norm_nn';data_zone2_norm_nn';data_zone3_norm_nn';data_zone4_norm_nn'];


%subplot_visualize(hfig,decreasedDataDuration,normalDuration,increaseDataDuration,decreasedDataArea,normalArea,increaseDataArea,plotNum1,plotNum2,connectionName);
%subplot_density_visualize(hfig,decreasedDataDuration,normalDuration,increaseDataDuration,decreasedDataArea,normalArea,increaseDataArea,plotNum1,plotNum2,connectionName);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
decreasedDataArea=[];increaseDataArea=[];decreasedDataDuration=[];increaseDataDuration=[];
data_zone1_duration=[];data_zone2_duration=[];data_zone3_duration=[];data_zone4_duration=[];
data_zone1_area=[];data_zone2_area=[];data_zone3_area=[];data_zone4_area=[];
data_zone1_norm=[];data_zone2_norm=[];data_zone3_norm=[];data_zone4_norm=[];
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
connectionName{6,1}='TI-STN';
decreasedDataDuration_temp=norm_Data_A_duration(31:31+2,:);
decreasedDataDuration=flipud(decreasedDataDuration_temp);
increaseDataDuration=norm_Data_A_duration(34:34+2,:);
plotNum1=6;
 
decreasedDataArea_temp=norm_data_B_Area(31:31+2,:);
decreasedDataArea=flipud(decreasedDataArea_temp);
increaseDataArea=norm_data_B_Area(34:34+2,:);
plotNum2=12;



data_zone1_duration=[decreasedDataDuration(:,1);normalDuration(1,1);increaseDataDuration(:,1)];
data_zone2_duration=[decreasedDataDuration(:,2);normalDuration(1,2);increaseDataDuration(:,2)];
data_zone3_duration=[decreasedDataDuration(:,3);normalDuration(1,3);increaseDataDuration(:,3)];
data_zone4_duration=[decreasedDataDuration(:,4);normalDuration(1,4);increaseDataDuration(:,4)];

data_zone_duration{6,:}=[data_zone1_duration';data_zone2_duration';data_zone3_duration';data_zone4_duration'];
%singleLoop{6,1}=[data_zone1_duration';data_zone2_duration';data_zone3_duration';data_zone4_duration'];
data_zone1_norm_dd=data_zone1_duration./data_zone1_duration(4,1);%
data_zone2_norm_dd=data_zone2_duration./data_zone2_duration(4,1);%
data_zone3_norm_dd=data_zone3_duration./data_zone3_duration(4,1);
data_zone4_norm_dd=data_zone4_duration./data_zone4_duration(4,1);
singleLoop{6,1}=[data_zone1_norm_dd';data_zone2_norm_dd';data_zone3_norm_dd';data_zone4_norm_dd'];

data_zone1_area=[decreasedDataArea(:,1);normalArea(1,1);increaseDataArea(:,1)];
data_zone2_area=[decreasedDataArea(:,2);normalArea(1,2);increaseDataArea(:,2)];
data_zone3_area=[decreasedDataArea(:,3);normalArea(1,3);increaseDataArea(:,3)];
data_zone4_area=[decreasedDataArea(:,4);normalArea(1,4);increaseDataArea(:,4)];


data_zone1_norm=data_zone1_area./data_zone1_duration;%(data_zone1 - (min(data_zone1))) / ( (max(data_zone1)) - (min(data_zone1)) );
data_zone2_norm=data_zone2_area./data_zone2_duration;%(data_zone2 - (min(data_zone2))) / ( (max(data_zone2)) - (min(data_zone2)) );
data_zone3_norm=data_zone3_area./data_zone3_duration;%(data_zone3 - (min(data_zone3))) / ( (max(data_zone3)) - (min(data_zone3)) );
data_zone4_norm=data_zone4_area./data_zone4_duration;%(data_zone4 - (min(data_zone4))) / ( (max(data_zone4)) - (min(data_zone4)) );


data_zone_area{6,:}=[data_zone1_norm';data_zone2_norm';data_zone3_norm';data_zone4_norm'];
%singleLoop{12,1}=[data_zone1_norm';data_zone2_norm';data_zone3_norm';data_zone4_norm'];

data_zone1_norm_nn=data_zone1_norm./data_zone1_norm(4,1);%
data_zone2_norm_nn=data_zone2_norm./data_zone2_norm(4,1);%
data_zone3_norm_nn=data_zone3_norm./data_zone3_norm(4,1);
data_zone4_norm_nn=data_zone4_norm./data_zone4_norm(4,1);
singleLoop{12,1}=[data_zone1_norm_nn';data_zone2_norm_nn';data_zone3_norm_nn';data_zone4_norm_nn'];


%subplot_visualize(hfig,decreasedDataDuration,normalDuration,increaseDataDuration,decreasedDataArea,normalArea,increaseDataArea,plotNum1,plotNum2,connectionName);
%subplot_density_visualize(hfig,decreasedDataDuration,normalDuration,increaseDataDuration,decreasedDataArea,normalArea,increaseDataArea,plotNum1,plotNum2,connectionName);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
disp('end') 


for ff=1:6
    if(ff==1)
    d1_snr=singleLoop{1,1};
    v1=d1_snr(:,1:3);
    vn=d1_snr(:,4);    
    v2=d1_snr(:,5:7);
    d1_snr_dur=horzcat(v1,v2,vn);
    d1_snr_dur=d1_snr_dur';
    d1_snr_dur_mean=mean(d1_snr_dur);
    d1_snr_dur_std=std(d1_snr_dur);
    d1_snr_dur_var=var(d1_snr_dur);  
    d1_snr_dur_std_cv=d1_snr_dur_std./d1_snr_dur_mean;
    d1_snr_dur_var_cv=d1_snr_dur_var./d1_snr_dur_mean;  

    d1_snr=singleLoop{7,1};
    v1=d1_snr(:,1:3);
    v2=d1_snr(:,5:7);
    vn=d1_snr(:,4);       
    d1_snr_area=horzcat(v1,v2,vn);
    d1_snr_area=d1_snr_area';
    d1_snr_area(find(isnan( d1_snr_area)==1))=0;
    d1_snr_area_mean=mean(d1_snr_area);
    d1_snr_area_std=std(d1_snr_area);
    d1_snr_area_var=var(d1_snr_area);  
    d1_snr_area_std_cv=d1_snr_area_std./d1_snr_area_mean;  
    d1_snr_area_var_cv=d1_snr_area_var./d1_snr_area_mean;    
    end
    
    if(ff==2)
    d2_ti=singleLoop{2,1};
    v1=d2_ti(:,1:3);
    v2=d2_ti(:,5:7);
    vn=d2_ti(:,4);      
    d2_ti_dur=horzcat(v1,v2, vn);
    d2_ti_dur=d2_ti_dur';
    d2_ti_dur_mean=mean(d2_ti_dur);
    d2_ti_dur_std=std(d2_ti_dur);
    d2_ti_dur_var=var(d2_ti_dur);  
    d2_ti_dur_std_cv=d2_ti_dur_std./d2_ti_dur_mean;
    d2_ti_dur_var_cv=d2_ti_dur_var./d2_ti_dur_mean;      
    
    

    d2_ti=singleLoop{8,1};
    v1=d2_ti(:,1:3);
    v2=d2_ti(:,5:7);
    vn=d2_ti(:,4);    
    d2_ti_area=horzcat(v1,v2, vn);
    d2_ti_area=d2_ti_area';
    d2_ti_area(find(isnan( d2_ti_area)==1))=0;
    d2_ti_area_mean=mean(d2_ti_area);
    d2_ti_area_std=std(d2_ti_area);
    d2_ti_area_var=var(d2_ti_area);  
    d2_ti_area_std_cv=d2_ti_area_std./d2_ti_area_mean;
    d2_ti_area_var_cv=d2_ti_area_var./d2_ti_area_mean;   
        
    end
    
    
        if(ff==3)
    ta_ti=singleLoop{3,1};
    v1=ta_ti(:,1:3);
    v2=ta_ti(:,5:7);
    vn=ta_ti(:,4);    
    ta_ti_dur=horzcat(v1,v2, vn);
    ta_ti_dur=ta_ti_dur';
    ta_ti_dur_mean=mean(ta_ti_dur);
    ta_ti_dur_std=std(ta_ti_dur);
    ta_ti_dur_var =var(ta_ti_dur);
    ta_ti_dur_std_cv=ta_ti_dur_std./ta_ti_dur_mean;
    ta_ti_dur_var_cv=ta_ti_dur_var./ta_ti_dur_mean;
    

    ta_ti=singleLoop{9,1};
    v1=ta_ti(:,1:3);
    v2=ta_ti(:,5:7);
    vn=ta_ti(:,4);  
    ta_ti_area=horzcat(v1,v2, vn);
    ta_ti_area=ta_ti_area';
    ta_ti_area(find(isnan( ta_ti_area)==1))=0;
    ta_ti_area_mean=mean(ta_ti_area);
    ta_ti_area_std=std(ta_ti_area);
    ta_ti_area_var=var(ta_ti_area);  
    ta_ti_area_std_cv=ta_ti_area_std./ta_ti_area_mean;
    ta_ti_area_var_cv=ta_ti_area_var./ta_ti_area_mean;
    
        end
    
          if(ff==4)
    ti_ta=singleLoop{4,1};
    v1=ti_ta(:,1:3);
    v2=ti_ta(:,5:7);
    vn=ti_ta(:,4);    
    ti_ta_dur=horzcat(v1,v2, vn);
    ti_ta_dur=ti_ta_dur';
    ti_ta_dur_mean=mean(ti_ta_dur);
    ti_ta_dur_std=std(ti_ta_dur);
    ti_ta_dur_var=var(ti_ta_dur);
    ti_ta_dur_std_cv=ti_ta_dur_std./ti_ta_dur_mean;
    ti_ta_dur_var_cv=ti_ta_dur_var./ti_ta_dur_mean;

    ti_ta=singleLoop{10,1};
    v1=ti_ta(:,1:3);
    v2=ti_ta(:,5:7);
    vn=ti_ta(:,4);     
    ti_ta_area=horzcat(v1,v2,vn);
    ti_ta_area=ti_ta_area';
    ti_ta_area(find(isnan(ti_ta_area)==1))=0;
    ti_ta_area_mean=mean(ti_ta_area);
    ti_ta_area_std=std(ti_ta_area);
    ti_ta_area_var=var(ti_ta_area);
    ti_ta_area_std_cv =ti_ta_area_std./ti_ta_area_mean;
    ti_ta_area_var_cv =ti_ta_area_var./ti_ta_area_mean;
          end   
    
    if(ff==5)
    stn_ti=singleLoop{5,1};
    v1=stn_ti(:,1:3);
    v2=stn_ti(:,5:7);
    vn=stn_ti(:,4);   
    stn_ti_dur=horzcat(v1,v2, vn);
    stn_ti_dur=stn_ti_dur';
    stn_ti_dur_mean=mean(stn_ti_dur);
    stn_ti_dur_std=std(stn_ti_dur);
    stn_ti_dur_var=var(stn_ti_dur);
    stn_ti_dur_std_cv=stn_ti_dur_std./stn_ti_dur_mean;
    stn_ti_dur_var_cv=stn_ti_dur_var./stn_ti_dur_mean;

    stn_ti=singleLoop{11,1};
    v1=stn_ti(:,1:3);
    v2=stn_ti(:,5:7);
    vn=stn_ti(:,4);  
    stn_ti_area=horzcat(v1,v2, vn);
    stn_ti_area=stn_ti_area';
    stn_ti_area(find(isnan(stn_ti_area)==1))=0;
    stn_ti_area_mean=mean(stn_ti_area);
    stn_ti_area_std=std(stn_ti_area);
    stn_ti_area_var=var(stn_ti_area);
    stn_ti_area_std_cv =stn_ti_area_std./stn_ti_area_mean;
    stn_ti_area_var_cv =stn_ti_area_var./stn_ti_area_mean;
     end 
    
                
    if(ff==6)
    ti_stn=singleLoop{6,1};
    v1=ti_stn(:,1:3);
    v2=ti_stn(:,5:7);
    vn=ti_stn(:,4);   
    ti_stn_dur=horzcat(v1,v2,vn);
    ti_stn_dur=ti_stn_dur';
    ti_stn_dur_mean=mean(ti_stn_dur);
    ti_stn_dur_std=std(ti_stn_dur);
    ti_stn_dur_var=var(ti_stn_dur);
    ti_stn_dur_std_cv=ti_stn_dur_std./ti_stn_dur_mean;
    ti_stn_dur_var_cv=ti_stn_dur_var./ti_stn_dur_mean;

    ti_stn=singleLoop{12,1};
    v1=ti_stn(:,1:3);
    v2=ti_stn(:,5:7);
    vn=ti_stn(:,4);  
    ti_stn_area=horzcat(v1,v2,vn);
    ti_stn_area=ti_stn_area';
    ti_stn_area(find(isnan(ti_stn_area)==1))=0;
    ti_stn_area_mean=mean(ti_stn_area);
    ti_stn_area_std=std(ti_stn_area);
    ti_stn_area_var=var(ti_stn_area);
    ti_stn_area_std_cv=ti_stn_area_std./ti_stn_area_mean;
    ti_stn_area_var_cv=ti_stn_area_var./ti_stn_area_mean;   
    end  
       
end
dur_Strength_mean =[d1_snr_dur_mean;d2_ti_dur_mean; ta_ti_dur_mean; ti_ta_dur_mean; stn_ti_dur_mean; ti_stn_dur_mean;];
dur_Strength_mean=dur_Strength_mean';
dur_Strength_mean_T=flipud(dur_Strength_mean);

dur_area_mean =[d1_snr_area_mean; d2_ti_area_mean; ta_ti_area_mean; ti_ta_area_mean; stn_ti_area_mean; ti_stn_area_mean;];
dur_area_mean=dur_area_mean';
dur_area_T =flipud(dur_area_mean);

%saveas(f,dest_path)
connectionName_T=connectionName'


dur_Strength_std =[d1_snr_dur_std_cv;d2_ti_dur_std_cv; ta_ti_dur_std_cv; ti_ta_dur_std_cv; stn_ti_dur_std_cv; ti_stn_dur_std_cv;];
dur_Strength_std=dur_Strength_std';
dur_Strength_std_T=flipud(dur_Strength_std);

area_U_std =[d1_snr_area_std_cv; d2_ti_area_std_cv; ta_ti_area_std_cv; ti_ta_area_std_cv; stn_ti_area_std_cv; ti_stn_area_std_cv;];
area_U_std=area_U_std';
area_U_std_T =flipud(area_U_std);
d1_snr_dur_std_cv=[];d2_ti_dur_std_cv=[];ta_ti_dur_std_cv=[];ti_ta_dur_std_cv=[];stn_ti_dur_std_cv=[];ti_stn_dur_std_cv=[];
d1_snr_area_std_cv=[];d2_ti_area_std_cv=[];ta_ti_area_std_cv=[];ti_ta_area_std_cv=[];stn_ti_area_std_cv=[];ti_stn_area_std_cv=[];

f = figure('Position', get(0, 'Screensize'));
subplot(2,2,1);
%mycolormap = customcolormap([0 0.5 1], {,'#fff1af','#de425b'});%
mycolormap = customcolormap([0 0.5 1], {'#848387','#adabb3','#c9c5d4'});%

colorbar;
colormap(mycolormap);



xx_labels=connectionName_T;
yy_labels={'LI','LE','EI','EE'};
yy_labels=yy_labels';

%heatmap(norm_data_A_flip, xx_labels, yy_labels, '%0.3f', 'TickAngle', 45,'ShowAllTicks', true,'TickFontSize', 12,'FontSize', 14,'Colorbar', true,'Colormap', 'summer');
[h1im h1text h1label]=heatmap(dur_Strength_std_T, xx_labels, yy_labels, '%0.3f', 'TickAngle', 45,'ShowAllTicks', true,'TickFontSize', 12,'FontSize', 11,'Colorbar', true,'GridLines', ':');
ylabel('CV of duration');


subplot(2,2,2);
yy_labels={'LI','LE','EI','EE'};
%heatmap(norm_data_B_flip, xx_labels, yy_labels, '%0.3f', 'TickAngle', 45,'ShowAllTicks', true,'TickFontSize', 12,'FontSize', 14,'Colorbar', true,'Colormap', 'summer');
[h2im h2text h2label]=heatmap(area_U_std_T, xx_labels, yy_labels, '%0.3f', 'TickAngle', 45,'ShowAllTicks', true,'TickFontSize', 12,'FontSize', 11,'Colorbar', true,'GridLines', ':');
ylabel('CV of area per unit time');
set(gcf,'Color',[1 1 1]); 
saveas(gca,'fig5_heatmap.png')

end


