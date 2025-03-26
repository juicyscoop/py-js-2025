DO $$
BEGIN
    -- Perform the update
    UPDATE employees
    SET salary = salary + 5000
    WHERE department = 'Sales';

    -- Check the number of affected rows and commit or rollback accordingly
    IF (SELECT count(*) FROM employees WHERE department = 'Sales') = 10 THEN
        COMMIT;
    ELSE
        ROLLBACK;
    END IF;
END $$;