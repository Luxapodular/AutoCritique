#pragma once

#include "ofxCcv.h"


float correlation(vector<float> & v1, vector<float> & v2);

class ofApp : public ofBaseApp {
public:
    void setup();
    void update();
    void draw();
    
    ofxCcv ccv;
    
    ofVideoGrabber grab;
};