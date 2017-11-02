
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%PROJECT OF FINANCIAL LAB 
%STUDENTS: Jaša Stefan, Laura Carvajal and Andraz Pirnovar
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function [area] = ProjectFinLab(r1,r2,N)
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%OBJECTIVE: Consider an annulus A, that is, A is the set of points between
% two concentric circles C and C'. Let us assume that C' is the smaller circle.
% Let P_n be a set of n points selected uniformly at random inside Analyze
% experimentally the length and the area of CH(P_n), the convex hull of P_n. 
% Analyze experimentally the probability that CH(P_n) contains C'. The results 
% should depend on the size of the annulus.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Input: 
% N:  number of points into our set
% rep:  number of times we compute P_n for calculate de probability 
% r1: Radius of the small circumference 
% r2: Radius of the big circumference 

% Output:
% area: the value of it's area
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

format short e %format of the numbers
%Create the graph that we need for make the algorithm 
figure;
t=linspace(0,2*pi,1000);
x=r1*cos(t);
y=r1*sin(t);
z=r2*cos(t);
w=r2*sin(t);
hold on
plot(x,y,'linewidth',2); %print the big circunference
hold on
plot(z,w,'linewidth',2); %print the small circunference

%Create the random numbers
k=1;
X=[];
while k <= N
    px=randi([-100*r1,100*r1])/100;
    py=randi([-100*r1,100*r1])/100;
    if sqrt(px^2+py^2) <= r1 & sqrt(px^2+py^2) >= r2
        plot(px,py,'.k') %print the random numbers
        hold on
        X(k,1)=px;
        X(k,2)=py;
        k=k+1;
    end
    axis([-(r1+1) r1+1 -(r1+1) r1+1]);
    axis('square'); 
end    
X1=X(:,1); 
X2=X(:,2);
%Compute de convex hull
[u,a] = convhull(X1,X2); 
area=a;
%plot the polynomial we are looking for 
plot(X1(u),X2(u),'k-') 
end

% For prove put in the command Window [prob,area]=trabajo(10,2,100)
% in this case for example is r1=10, r2=2, N=100, but you can put otgher
% numbers
