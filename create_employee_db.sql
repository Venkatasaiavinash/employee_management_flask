CREATE DATABASE Employeedb;
GO
USE Employeedb;
GO
CREATE TABLE Employees (
    EmployeeID INT IDENTITY(1,1) PRIMARY KEY,
    FullName   NVARCHAR(90)  NOT NULL,
    Email      NVARCHAR(90)  NOT NULL UNIQUE,
    Department NVARCHAR(30)  NOT NULL,
    Status     NVARCHAR(30)  NOT NULL DEFAULT 'On Boarding',
    CreatedAt  DATETIME      NOT NULL DEFAULT GETDATE()
);
GO
INSERT INTO Employees (FullName, Email, Department, Status) VALUES
('Avinash', 'venkatasaiavinashsandu@gmail.com', 'IT', 'Active'),
('Akash',   'Akash@gmail.com',                  'HR', 'On Boarding');
GO