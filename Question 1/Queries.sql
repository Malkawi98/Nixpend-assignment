SELECT COUNT(Patient_ID) AS "patient_count",
       Patient_ID,
       CASE
           WHEN m.Expiration_Date < CURRENT_DATE THEN 'Expired'
           ELSE 'Active'
           END           AS MedicationStatus
FROM medication AS m
         LEFT JOIN medication_prescribed mp ON m.Medication_ID = mp.medication_id
GROUP BY m.Medication_ID, mp.Patient_ID;

----------------------

SELECT d.doctor_id,
       d.Field     AS doctor_field,
       d.degree    AS doctor_degree,
       w.name      AS doctor_name,
       dp.Time     AS appointment_time,
       p.patient_id AS patient_id,
       p.Name      AS patient_name,
       p.Age       AS patient_age,
       dpt.workers AS department_workers
FROM doctor d
         JOIN
     doctor_patient dp ON d.doctor_id = dp.doctor_id
         JOIN
     patient p ON dp.patient_id = p.patient_d
         JOIN
     department dpt ON d.Department = dpt.department_id
         JOIN worker w ON d.doctor_id = w.worker_id
WHERE p.Age > 12
  AND EXTRACT(YEAR FROM dp.Time) != 2022
ORDER BY w.name DESC, p.Name;

