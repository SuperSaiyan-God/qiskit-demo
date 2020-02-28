from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister

q0 = QuantumRegister(4, 'q0')
c0 = ClassicalRegister(2, 'c0')
q1 = QuantumRegister(4, 'q1')
c1 = ClassicalRegister(2, 'c1')
q2 = QuantumRegister(4, 'q2')
q_test = QuantumRegister(2, 'q_test')

sub_circuit = QuantumCircuit(q0, name='sub_circ')
sub_circuit.cx(q0[0],q0[2])
sub_circuit.cx(q0[1],q0[2])
sub_circuit.x(q0[2])
sub_circuit.x(q0[1])
sub_circuit.ccx(q0[0],q0[1],q0[3])
sub_circuit.x(q0[1])

sub_circuit.draw(output='mpl')

register = sub_circuit.to_instruction()

q = QuantumRegister(14, 'q')

a0 = QuantumCircuit(q)

a0.append(register, [q[0],q[1],q[2],q[3]])
a0.append(register, [q[4],q[5],q[6],q[7]])
a0.append(register, [q[8],q[9],q[10],q[11]])

a0.draw(output='mpl')