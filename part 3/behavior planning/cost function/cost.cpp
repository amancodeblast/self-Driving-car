https://docs.google.com/forms/d/1TeitWQ3JnJTjrP4eXlZdGOwSGL1k2GoMfqbWKE3eCnE/edit#include <functional>
#include <iostream>
#include "cost.h"
#include "cmath"


using namespace std;

float goal_distance_cost(int goal_lane, int intended_lane, int final_lane, float distance_to_goal) {
    /*
    The cost increases with both the distance of intended lane from the goal
    and the distance of the final lane from the goal. The cost of being out of the 
    goal lane also becomes larger as vehicle approaches the goal.
    */
    
    //TODO: Replace cost = 0 with an appropriate cost function.
    float cost = 0;
    float del_d=abs(2*goal_lane-intended_lane-final_lane);
    cost+= 1-exp(-(del_d/distance_to_goal))
    return cost;
}
