import os
import numpy as np
os.system("gcc -o bin/mnist-dnn-5-layer -Iutil  main_5_layer.c dnn.c util/screen.c util/mnist-utils.c util/mnist-stats.c -lm -std=c99")


layer1_width = 1
layer1_height = 2
layer1_depth = 3
layer1_filter = 4
layer2_width= 5
layer2_height = 6
layer2_depth = 7
layer2_filter = 8
"""
for  layer1_width in range(6, 20):
    for layer1_depth in range(5, 10):
        for layer1_filter in range(4, 7):
            layer2_width = layer1_width  
            for layer2_depth in range(layer1_depth+4, layer1_depth + 20):
                for layer2_filter in range(4, 7):
                    print layer1_width, layer1_depth, layer1_filter, layer2_width, layer2_depth, layer2_filter
"""
os.system("rm results_5_layer");
for  layer1_width in range(13, 14, 2):
    for layer1_depth in range(5, 6):
        for layer1_filter in range(5, 6):
            layer2_width = 6 
            for layer2_depth in range(5,6):
                for layer2_filter in range(3, 4):
                    os.system("echo **************** >> results_5_layer")
                    os.system("echo ****************START >> results_5_layer")
                    for learning_rate in np.arange(.00014, .00022, .0001):
                        for iteration in range(0, 1):
                            os.system("./bin/mnist-dnn-5-layer " + str(layer1_width) + " " + str(layer1_depth) + " " + str(layer1_filter) + " " + str(layer2_width) + " " + str(layer2_depth) + " " +
                                    str(layer2_filter) + " " + str(learning_rate) + " >> results_5_layer")
                            os.system("echo ****************INTERNAL_DONE>> results_5_layer")
                        os.system("echo ****************DONE >> results_5_layer")
