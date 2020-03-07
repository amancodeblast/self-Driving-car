// In this quiz you'll implement the global kinematic model.
#include <math.h>
#include <iostream>
#include "Dense"

//
// Helper functions
//
double pi() { return M_PI; }
double deg2rad(double x) { return x * pi() / 180; }
double rad2deg(double x) { return x * 180 / pi(); }

const double Lf = 2;


Eigen::VectorXd globalKinematic(Eigen::VectorXd state,
                                Eigen::VectorXd actuators, double dt) {
  Eigen::VectorXd next_state(state.size());
  
  //TODO: Implement the Global Kinematic Model, to return
  // the next state from inputs

  // NOTE: state is [x, y, psi, v]
  // NOTE: actuators is [delta, a]
  
  //Add your code below
  int xs,ys,psis,velocity,deltas, acc;
  xs=state(0);
  ys=state(1);
  psis=state(2);
  velocity=state(3);
  deltas=actuators(0);
  acc=actuators(1);
  next_state[]=xs+cos(psis)*dt*velocity;
  yn=ys+sin(psis)*dt*velocity;
  psin=psis+velocity*acc*dt/Lf;
  vn=velocity+acc*dt;
  next_state=[xn,yn,psin,vn];next_state[0] = state[0] + state[3] * cos(state[2])*dt;
  next_state[1] = state[1] + state[3] * sin(state[2])*dt;
  next_state[2] = state[2] + state[3]/Lf *actuators[0]*dt;
  next_state[3] = state[3] + actuators[1]*dt;

  return next_state;
}

int main() {
  // [x, y, psi, v]
  Eigen::VectorXd state(4);
  // [delta, v]
  Eigen::VectorXd actuators(2);

  state << 0, 0, deg2rad(45), 1;
  actuators << deg2rad(5), 1;

  Eigen::VectorXd next_state = globalKinematic(state, actuators, 0.3);

  std::cout << next_state << std::endl;
}