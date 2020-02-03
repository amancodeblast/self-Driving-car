#include <iostream>
#include "ukf.h"

UKF::UKF() {
  //TODO Auto-generated constructor stub
  Init();
}

UKF::~UKF() {
  //TODO Auto-generated destructor stub
}

void UKF::Init() {

}


/*******************************************************************************
* Programming assignment functions: 
*******************************************************************************/

void UKF::SigmaPointPrediction(MatrixXd* Xsig_out) {

  //set state dimension
  int n_x = 5;

  //set augmented dimension
  int n_aug = 7;

  //create example sigma point matrix
  MatrixXd Xsig_aug = MatrixXd(n_aug, 2 * n_aug + 1);
     Xsig_aug <<
    5.7441,  5.85768,   5.7441,   5.7441,   5.7441,   5.7441,   5.7441,   5.7441,   5.63052,   5.7441,   5.7441,   5.7441,   5.7441,   5.7441,   5.7441,
      1.38,  1.34566,  1.52806,     1.38,     1.38,     1.38,     1.38,     1.38,   1.41434,  1.23194,     1.38,     1.38,     1.38,     1.38,     1.38,
    2.2049,  2.28414,  2.24557,  2.29582,   2.2049,   2.2049,   2.2049,   2.2049,   2.12566,  2.16423,  2.11398,   2.2049,   2.2049,   2.2049,   2.2049,
    0.5015,  0.44339, 0.631886, 0.516923, 0.595227,   0.5015,   0.5015,   0.5015,   0.55961, 0.371114, 0.486077, 0.407773,   0.5015,   0.5015,   0.5015,
    0.3528, 0.299973, 0.462123, 0.376339,  0.48417, 0.418721,   0.3528,   0.3528,  0.405627, 0.243477, 0.329261,  0.22143, 0.286879,   0.3528,   0.3528,
         0,        0,        0,        0,        0,        0,  0.34641,        0,         0,        0,        0,        0,        0, -0.34641,        0,
         0,        0,        0,        0,        0,        0,        0,  0.34641,         0,        0,        0,        0,        0,        0, -0.34641;

  //create matrix with predicted sigma points as columns
  MatrixXd Xsig_pred = MatrixXd(n_x, 2 * n_aug + 1);

  double delta_t = 0.1; //time diff in sec

/*******************************************************************************
 * Student part begin
 ******************************************************************************/
for(int i=0;i<n_aug;i++){
 double p_x=Xsig_aug(0,i);
 double p_y=sig_aug(1,i);
 double v=sig_aug(2,i);
 double Sie=sig_aug(3,i);
 double Sie_dot=sig_aug(4,i);
 double nu_a=sig_aug(5,i);
 double nu_sie=sig_aug(6,i);
double p_y_k,p_x_k;
if(Sie_dot<0.001){
p_x_k=p_x+v/Sie_dot*(sin(Sie+Sie_dot*delta_t)-sin(Sie));
p_x_k=p_x+v/Sie_dot*(-cos(Sie+Sie_dot*delta_t)+cos(Sie));

}
else{
  p_x_k=p_x+v*cos(sie)*delta_t;
  p_y_k=p_y+v*cos(sie)*delta_t;

}
 p_x_k=p_x_k+(delta_t*delta_t*cos(sie)*nu_a)/2;
 p_y_k=p_y_k+(delta_t*delta_t*sin(sie)*nu_a)/2:
 v_k=delta_t*nu_a;
 Sie_k=Sie_dot*delta_t+(nu_sie*delta_t*delta_t)/2;
 Sie_dot_k=delta_t*nu_sie;

 Xsig_pred(0,i)=p_x_k;
 Xsig_pred(1,i)=p_y_k;
 Xsig_pred(2,i)=v_k;
 Xsig_pred(3,i)=Sie_k;
 Xsig_pred(4,i)=Sie_dot_k;
 
}

  //predict sigma points
  //avoid division by zero
  //write predicted sigma points into right column
  

/*******************************************************************************
 * Student part end
 ******************************************************************************/

  //print result



d::cout << "Xsig_pred = " << std::endl << Xsig_pred << std::endl;

  //write result
  *Xsig_out = Xsig_pred;

}