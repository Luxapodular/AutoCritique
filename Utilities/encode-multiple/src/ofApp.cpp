#include "ofApp.h"


void ofApp::setup() {
    //ccv.setup("image-net-2012-vgg-d.sqlite3");
    string pathToImages = "images/";
    string pathToFeatures = "features/";
    ccv.setup("image-net-2012.sqlite3");
    
    // Load directory. Only allow pngs and jpgs.
    ofDirectory dir(pathToImages);
    dir.allowExt("jpg");
    dir.allowExt("png");
    dir.listDir();
    
    // Go through directory.
    for (int i = 0; i < dir.size(); i++) {
        ofImage img;
        string imgPath = dir.getPath(i);
        img.load(imgPath);
        
        // Encode image features as a vector of floats. Take second to last
        // layer in order to get as many feature points as possible.
        vector<float> imgFeatures = ccv.encode(img, ccv.numLayers()-1);
        
        ofFile file;
        ofBuffer buffer;
        
        // Store a buffer with each feature point on a single line.
        for (float f : imgFeatures) {
            buffer.append(ofToString(f));
            buffer.append("\n");
        }
        
        // Output that buffer to a .txt file for further processing.
        ofBufferToFile(pathToFeatures + dir.getName(i) + ".txt", buffer);
    }
}

void ofApp::update() {
}

void ofApp::draw() {
    ofBackground(0);
}

float correlation(vector<float> & v1, vector<float> & v2) {
    // pearson correlation
    int n = v1.size();
    float s1=0, s12=0, s2=0, s22=0, s1s2=0;
    for (int i=0; i<n; i++) {
        s1 += v1[i];
        s2 += v2[i];
        s12 += pow(v1[i], 2);
        s22 += pow(v2[i], 2);
        s1s2 += (v1[i] * v2[i]);
    }
    float r = (n * s1s2 - s1 * s2) / (sqrt(n * s12 - pow(s1, 2)) * sqrt(n * s22 - pow(s2, 2)));
    return r;
}
