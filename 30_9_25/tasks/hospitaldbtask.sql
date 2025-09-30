Create database HospitalDB;
Use HospitalDB;

create table Patients(
patient_id INT PRIMARY KEY,
name VARCHAR(50),
age INT,
gender CHAR(1),
city VARCHAR(50));

create table Doctors(
doctor_id INT PRIMARY KEY,
name VARCHAR(50),
specialization VARCHAR(50),
experience INT);

create table appointments(
appointment_id INT PRIMARY KEY,
patient_id int,
doctor_id int,
FOREIGN KEY (patient_id)  references Patients(patient_id),
FOREIGN KEY (doctor_id) references Doctors(doctor_id),
appointment_date DATE,
status VARCHAR(20));

create table MedicalRecord(
record_id INT PRIMARY KEY,
patient_id int,
doctor_id int,
FOREIGN KEY (patient_id) references Patients(patient_id),
FOREIGN KEY(doctor_id ) references Doctors(doctor_id),
diagnosis VARCHAR(100),
treatment VARCHAR(100),
date DATE);

create table billing(
patient_id int,
doctor_id int,
bill_id INT PRIMARY KEY,
FOREIGN KEY (patient_id ) references Patients(patient_id),
amount DECIMAL(10,2),
bill_date DATE,
status VARCHAR(20));

INSERT INTO Patients (patient_id, name, age, gender, city) VALUES
(101, 'Ananya Sharma', 35, 'F', 'Mumbai'),
(102, 'Ramesh Singh', 52, 'M', 'Delhi'),
(103, 'Priya Menon', 28, 'F', 'Bengaluru'),
(104, 'Vikram Reddy', 60, 'M', 'Hyderabad'),
(105, 'Kavita Das', 41, 'F', 'Kolkata'),
(106, 'Sanjay Patel', 19, 'M', 'Ahmedabad'),
(107, 'Meera Iyer', 70, 'F', 'Chennai'),
(108, 'Aditya Choudhary', 22, 'M', 'Pune'),
(109, 'Jaya Prasad', 48, 'F', 'Lucknow'),
(110, 'Naveen Kumar', 30, 'M', 'Jaipur');

INSERT INTO Doctors (doctor_id, name, specialization, experience) VALUES
(201, 'Dr. Sunita Rao', 'Cardiology', 15),
(202, 'Dr. Arjun Mehta', 'Orthopedics', 10),
(203, 'Dr. Tara Gupta', 'Pediatrics', 8),
(204, 'Dr. Rohan Nambiar', 'Neurology', 25),
(205, 'Dr. Fatima Khan', 'Dermatology', 6);

INSERT INTO Appointments (appointment_id, patient_id, doctor_id, appointment_date, status) VALUES
(301, 101, 201, '2025-10-05', 'Scheduled'),   -- Ananya Sharma (Mumbai) with Dr. Sunita Rao (Cardiology)
(302, 102, 202, '2025-10-06', 'Completed'),   -- Ramesh Singh (Delhi) with Dr. Arjun Mehta (Orthopedics)
(303, 103, 203, '2025-10-06', 'Completed'),   -- Priya Menon (Bengaluru) with Dr. Tara Gupta (Pediatrics)
(304, 104, 204, '2025-10-07', 'Scheduled'),   -- Vikram Reddy (Hyderabad) with Dr. Rohan Nambiar (Neurology)
(305, 105, 205, '2025-10-07', 'Scheduled'),   -- Kavita Das (Kolkata) with Dr. Fatima Khan (Dermatology)
(306, 106, 202, '2025-10-08', 'Canceled'),    -- Sanjay Patel (Ahmedabad) with Dr. Arjun Mehta (Orthopedics)
(307, 107, 201, '2025-10-08', 'Completed'),   -- Meera Iyer (Chennai) with Dr. Sunita Rao (Cardiology)
(308, 108, 203, '2025-10-09', 'Scheduled'),   -- Aditya Choudhary (Pune) with Dr. Tara Gupta (Pediatrics)
(309, 109, 204, '2025-10-10', 'Scheduled'),   -- Jaya Prasad (Lucknow) with Dr. Rohan Nambiar (Neurology)
(310, 110, 205, '2025-10-10', 'Canceled');    -- Naveen Kumar (Jaipur) with Dr. Fatima Khan (Dermatology)

INSERT INTO MedicalRecord (record_id, patient_id, doctor_id, diagnosis, treatment, date) VALUES
(401, 101, 201, 'Mild Hypertension', 'Prescribed Atenolol 50mg, dietary changes', '2025-10-05'),  -- Patient 101, Dr. 201
(402, 102, 202, 'Torn Meniscus (Knee)', 'Physiotherapy, scheduled follow-up surgery', '2025-10-06'), -- Patient 102, Dr. 202
(403, 103, 203, 'Viral Fever', 'Rest, hydration, Paracetamol', '2025-10-06'),                   -- Patient 103, Dr. 203
(404, 107, 201, 'Chronic Angina', 'Adjusted Nitroglycerin dosage, stress test scheduled', '2025-10-08'), -- Patient 107, Dr. 201
(405, 104, 204, 'Migraine Headaches', 'Prescribed Sumatriptan, advised lifestyle changes', '2025-10-07'), -- Patient 104, Dr. 204 (Scheduled appointment assumed to have been completed)
(406, 105, 205, 'Eczema Flare-up', 'Topical corticosteroid cream, avoidance of irritants', '2025-10-07'), -- Patient 105, Dr. 205 (Scheduled appointment assumed to have been completed)
(407, 108, 203, 'Routine Child Check-up', 'Vaccination administered, growth assessment', '2025-10-09'); -- Patient 108, Dr. 203 (Scheduled appointment assumed to have been completed)

INSERT INTO billing (bill_id, patient_id, amount, bill_date, status) VALUES
(501, 101, 2500.00, '2025-10-05', 'Paid'),      -- Ananya Sharma (Hypertension check-up)
(502, 102, 12500.50, '2025-10-06', 'Unpaid'),    -- Ramesh Singh (Knee injury diagnosis)
(503, 103, 1500.00, '2025-10-06', 'Paid'),      -- Priya Menon (Viral fever consult)
(504, 107, 3200.00, '2025-10-08', 'Unpaid'),    -- Meera Iyer (Chronic Angina consult)
(505, 104, 4500.00, '2025-10-07', 'Paid'),      -- Vikram Reddy (Migraine consultation)
(506, 105, 1800.00, '2025-10-07', 'Paid'),      -- Kavita Das (Eczema treatment)
(507, 108, 950.00, '2025-10-09', 'Unpaid');     -- Aditya Choudhary (Child check-up/vaccination)

-- step 3 task 1
select p.patient_id, p.name, m.doctor_id,d.specialization
from medicalRecord m
join Patients p on m.patient_id = p.patient_id
join Doctors d on m.doctor_id = d.doctor_id
where d.specialization = "Cardiology";

-- step 3 task 2
select p.patient_id,p.name,a.appointment_id,a.appointment_date,d.doctor_id
from appointments a
join Patients p on a.patient_id = p.patient_id
join Doctors d on a.doctor_id = d.doctor_id;

-- step 3 task 3
select p.patient_id,p.name,b.bill_id,b.bill_date,b.status
from billing b
join patients p on p.patient_id=b.patient_id
where b.status='unpaid';

-- step 4 task 1
DELIMITER $$
create procedure  GetPatientHistory2(in pid int)
begin
select p.patient_id,p.name ,a.appointment_id,a.appointment_date,m.diagnosis,m.treatment
from MedicalRecord m
join Appointments a on m.patient_id=a.patient_id
join Patients p on p.patient_id=m.patient_id
where m.patient_id=pid;
END $$
DELIMITER ;

call GetPatientHistory2(101)

-- step 4 task 2
 DELIMITER $$
create procedure  GetDoctorAppointmentt(in docid int)
begin
select d.doctor_id,d.name,p.patient_id,p.name ,a.appointment_id,a.appointment_date
from Appointments  a
join Doctors d on d.doctor_id=a.doctor_id
join Patients p on a.patient_id=p.patient_id
where a.doctor_id=docid;
END $$
DELIMITER ;

call GetDoctorAppointmentt(202)
