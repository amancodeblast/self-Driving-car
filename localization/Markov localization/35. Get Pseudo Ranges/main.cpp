#include <iostream>
#include <algorithm>
#include <vector>

#include "helpers.h"
using namespace std;

//set standard deviation of control:
float control_stdev = 1.0f;

//meters vehicle moves per time step
float movement_per_timestep = 1.0f;

//number of x positions on map
int map_size = 25;

//define landmarks
std::vector<float> landmark_positions {5, 10, 12, 20};



std::vector<float> pseudo_range_estimator(std::vector<float> landmark_positions, float pseudo_position);


int main() {    
    
    //step through each pseudo position x (i)
    for (unsigned int i = 0; i < map_size; ++i) {
        float pseudo_position = float(i);
        //get pseudo ranges
        std::vector<float> pseudo_ranges = pseudo_range_estimator(landmark_positions, pseudo_position);

       //print to stdout
        if (pseudo_ranges.size() >0) {
            for (unsigned int s = 0; s < pseudo_ranges.size(); ++s) {
                std::cout << "x: " << i << "\t" << pseudo_ranges[s] << endl;
            }
            std::cout << "-----------------------" << endl;
        }   
    } 

    return 0;
};

//TODO: Complete pseudo range estimator function
std::vector<float> pseudo_range_estimator(std::vector<float> landmark_positions, float pseudo_position) {
    
    //define pseudo observation vector:
    std::vector<float> pseudo_ranges;
            
    //loop over number of landmarks and estimate pseudo ranges:
        //YOUR CODE HERE
        for(int i=0; i<landmark_positions.size();i++){
            float l=landmark_positions[i]-pseudo_position;
            if(l>0)
            {
                pseudo_ranges.push_back(l);
            }
        }

    //sort pseudo range vector:
        //YOUR CODE HERE
    std::sort(pseudo_ranges.begin(),pseudo_ranges.end());
    
    return pseudo_ranges;
}