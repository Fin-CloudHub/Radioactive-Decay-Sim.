#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 19:09:41 2024

@author: finlaysime 

"""
import math as m
import random as r

class Material:
    
    def __init__(self):
        """
        
        Constucts the 2D grid
        
        """
        N = input("What is your chosen value of N for the grid size: ")
        N = int(N)
        
        self.grid = []
        for i in range(N):
            self.grid.append([]) #Adds rows to the grid
            for j in range(N):
                self.grid[i].append(1) #Fills rows with ones  
        
                
    def __str__(self):
        """"
        Prints the 2D grid in the correct format
        
        """
        s = ""
        for row in self.grid:
            for point in row:
                s += f"{point} " #Print points
            s += "\n" #New line for next set of points
        return s
    
        
        
            

class Simulation:
    
    def __init__(self, N):
        """
        
        Constucts the 2D grid
        
        """
        
        self.grid = []
        for i in range(N):
            self.grid.append([]) #Adds rows to the grid
            for j in range(N):
                self.grid[i].append(1) #Fills rows with zeros      
                
                
    def __str__(self):
        """"
        Prints the 2D grid in the correct format
        
        """
        s = ""
        for row in self.grid:
            for point in row:
                s += f"{point} " #Print points
            s += "\n" #New line for next set of points
        return s
    
    def runsim(material, lamda, delta_t):
        """
        Runs a loop for set of decays
        
        """
        p = -lamda * delta_t #Calculates probability
        "Create variables for loop, time, number of decayed (no)"
        time = 0 
        no = 0
        while True: #Create loop that runs simulation for ear time step
            a = r.random()
            b = r.randint(0, len(material.grid[0])-1)
            c = r.randint(0, len(material.grid[0])-1)
            if material.grid[c][b] == 1 and abs(p) <= abs(a/1000): #Conditions to determine 
                   material.grid[c][b] = 0                         #if the nuclei has decayed
                   no += 1                                         #and if the probability 
                                                                   #can decay it
                    
            elif no == (len(material.grid[0])**2)/2: #Determines if half of nuclei have decayed
                tau = 1/lamda
                N = len(material.grid[0])
                print(f"The original number of undecayed nuclei was {N**2}")
                print(f"The final number of undecayed nuclei is {no}")
                print(f"The half-life of the material is {time} minutes")
                print(f"The actual half-life of the material is {tau} minutes")
                break
                    
            time += delta_t #Add time step to time at end of each loop
            print(material) #Print new nuclei set after decay
                        
        return time, no 
        
        
if __name__ == "__main__":
    """
    Test code for running simulation
    
    """
    #N = int(input("What is your chosen value of N: "))
    lamda = 0.02775
    delta_t = 0.01
    testgrid = Material()
    print(testgrid)
    Simulation.runsim(testgrid, lamda, delta_t)
    
    
