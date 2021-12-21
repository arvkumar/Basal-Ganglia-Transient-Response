function Fig5()
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
close all;

 A=load('zone_duration.txt');
 B=load('zone_area.txt');


AA_dur=A(:,2:2:8);
BB_area=abs(B);

%normal_row=[8	3	11	6	17	8	25	14];
%normal_Area=[160.822	37.851	725.68	309.3766];
normal_row =[7.0000    4.0000   11.0000    6.0000   17.0000    9.3000   26.3000   10.6100]
normal_Area =[258.3304   36.1512  710.2501  276.4640]

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

use_panel = 1;
clf

% PREPARE
if use_panel
	p = panel();
	%p.pack(N, N);
    p.pack(2, 6);
end
color_code={'#00876c', '#64c98a', '#b2cb99', '#f0edc0', '#e3ba68', '#e07c1f', '#de0000'};%set14
%color_code={'#003f5c', '#374c80', '#7a5195', '#bc5090', '#ef5675', '#ff764a', '#ffa600'};
%color_code={'#ffff00', '#fffa63', '#fff696', '#fff3c4', '#ccaa7a', '#9b633e', '#661d12'};


cntGraph=1;
%set(gcf,'position',[0, 0,1024,468]);
%figure('DefaultAxesFontSize',14)
for m = 1:2%N
    %cntGraph=1;
    label_name=1;
	for n = 1:6%N
		
            % select one of the NxN grid of sub-panels
            if use_panel
                sp=p(m, n).select();
            else
                subplot(N, N, m + (n-1) * N);
                %set(gca,'fontsize',20)
            end		
            %b = bar(data_zone_duration,'FaceColor','flat');
            b = bar(sp,singleLoop{cntGraph,1},'FaceColor','flat');
            %hold on;
            str=color_code{1};
            color = sscanf(str(2:end),'%2x%2x%2x',[1 3])/255;
            b(1).FaceColor = color;
            %b(1).EdgeColor = color;
            b(1).BarWidth=1.0;
            b(1).LineWidth=.001;
            %b(1).BarWidth=0.8;

            str=color_code{2};
            color = sscanf(str(2:end),'%2x%2x%2x',[1 3])/255;
            b(2).FaceColor = color;
            b(2).BarWidth=1.0;
            b(2).LineWidth=.001;

            %b(2).EdgeColor=color;

            str=color_code{3};
            color = sscanf(str(2:end),'%2x%2x%2x',[1 3])/255;
            b(3).FaceColor = color;
            b(3).BarWidth=1.0;
            b(3).LineWidth=.001;
            %b(3).EdgeColor=color;

            str=color_code{4};
            color = sscanf(str(2:end),'%2x%2x%2x',[1 3])/255;
            b(4).FaceColor = color;
            b(4).BarWidth=1.0;
            b(4).LineWidth=.001;
            %b(4).EdgeColor=color;

            str=color_code{5};
            color = sscanf(str(2:end),'%2x%2x%2x',[1 3])/255;
            b(5).FaceColor = color;
            b(5).BarWidth=1.0;
            b(5).LineWidth=.001;
            %b(5).EdgeColor=color;

            str=color_code{6};
            color = sscanf(str(2:end),'%2x%2x%2x',[1 3])/255;
            b(6).FaceColor = color;
            b(6).BarWidth=1.0;
            b(6).LineWidth=.001;
            %b(6).EdgeColor=color;

            str=color_code{7};
            color = sscanf(str(2:end),'%2x%2x%2x',[1 3])/255;
            b(7).FaceColor = color;
            b(7).BarWidth=1.0;
            b(7).LineWidth=.001;

            str = '#EAEAEA';%#FF0000';
            bgcolor = sscanf(str(2:end),'%2x%2x%2x',[1 3])/255;
            %set(gca,'Color',bgcolor)
            
                        % and so on - generally, you can treat the axis panel
                        % like any other axis
                        %axis([0 100 -3 3]);
                       % xTickLocations = linspace(1, 4, 4);
            xlabel={'EE', 'EI', 'LE', 'LI'};
            xTickLocations = linspace(1, 4, 4);
            set(sp,'XTick',xTickLocations,'XTickLabel', xlabel,'fontweight','bold');
            %set(gca,'fontweight','bold','fontsize',20);
            %set(gca,'FontSize',30)
            %ax = gca;
            sp.FontSize = 11;
            sp.FontWeight = 'Bold';
            title(connectionName{label_name,1});
            if(cntGraph==1)||(cntGraph==7)
                disp ('plotted')
                %legend('v - (v-v/m)* 3/3','v - (v-v/m)* 2/3', 'v - (v-v/m)* 1/3', 'Normal', 'v + (v*m-v)* 3/3', 'v + (v*m-v)* 2/3', 'v + (v*m-v)* 1/3','fontsize',14);
                %legend('v - (v-v/m)* 3/3','v - (v-v/m)* 2/3', 'v - (v-v/m)* 1/3', 'Normal', 'v + (v*m-v)* 1/3', 'v + (v*m-v)* 2/3', 'v + (v*m-v)* 3/3','fontsize',11);
                 if(m==1)
                ylabel('Duration (in ms)');%FontType','Times New Roman'
                 else
                ylabel('Area per unit time');
                 end
           % else
           %     ylabel('Area per unit time');%
            end
            axis tight;
            cntGraph=cntGraph+1;
            label_name=label_name+1;
	end
end

set(gcf, 'InvertHardCopy', 'off');
set(gcf,'Color',[1 1 1]); 
v1='\boldmath {$v -\frac{3}{3}(v-\frac{v}{m})$}';
v2='\boldmath {$v -\frac{2}{3}(v-\frac{v}{m})$}';
v3='\boldmath {$v -\frac{1}{3}(v-\frac{v}{m})$}';
v4='\it{\textbf{Normal(v)}}';
v5='\boldmath {$v +\frac{1}{3}(mv-v)$}';
v6='\boldmath {$v +\frac{2}{3}(mv-v)$}';
v7='\boldmath {$v +\frac{3}{3}(mv-v)$}';
leg1=legend(v1,v2,v3,v4,v5,v6,v7,'Interpreter','latex','AutoUpdate','off','fontweight', 'bold');
set(leg1,'Interpreter','latex','FontWeight','bold','FontSize',12);
set(leg1,'FontWeight','bold');
saveas(gca,'fig5.png')
%dest_path=strcat(dest_folder,'\','Figure_', 'TH_',num2str(TH), '_',channel_Act,'_AS', '.png')
%saveas(f,dest_path)

end


