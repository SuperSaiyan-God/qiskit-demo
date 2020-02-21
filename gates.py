from qiskit import *
from qiskit.tools.visualization import plot_histogram
import numpy as np

def NOT(input):

    q = QuantumRegister(1)
    c = ClassicalRegister(1)
    qc = QuantumCircuit(q, c)
    
    if input=='1':
        qc.x( q[0] )
        
    qc.x( q[0] )
    
    qc.measure( q[0], c[0] )
    
    backend = Aer.get_backend('qasm_simulator')
    job = execute(qc,backend,shots=1)
    output = next(iter(job.result().get_counts()))
    
    return output

def XOR(input1,input2):
    
    q = QuantumRegister(2)
    c = ClassicalRegister(1)
    qc = QuantumCircuit(q, c)
       
    qc.measure(q[1],c[0])
    
    backend = Aer.get_backend('qasm_simulator')
    job = execute(qc,backend,shots=1,memory=True)
    output = job.result().get_memory()[0]
    
    return output

def AND(input1,input2):
    
    q = QuantumRegister(3)
    c = ClassicalRegister(1)
    qc = QuantumCircuit(q, c)
    
    qc.measure(q[2],c[0])
    
    backend = Aer.get_backend('qasm_simulator')
    job = execute(qc,backend,shots=1,memory=True)
    output = job.result().get_memory()[0]
    
    return output

def NAND(input1,input2):
  
    q = QuantumRegister(3)
    c = ClassicalRegister(1)
    qc = QuantumCircuit(q, c)
    
    qc.measure(q[2],c[0])
    
    backend = Aer.get_backend('qasm_simulator')
    job = execute(qc,backend,shots=1,memory=True)
    output = job.result().get_memory()[0]
    
    return output

def OR(input1,input2):
  
    q = QuantumRegister(3)
    c = ClassicalRegister(1)
    qc = QuantumCircuit(q, c)
    
    qc.measure(q[2],c[0])
    
    backend = Aer.get_backend('qasm_simulator')
    job = execute(qc,backend,shots=1,memory=True)
    output = job.result().get_memory()[0]
    
    return output