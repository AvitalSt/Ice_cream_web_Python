USE ice_cream_db

-- הוספת נתונים לטבלת customers
INSERT INTO customers (user_name, password) VALUES
('JohnDoe', 'password123'),
('JaneDoe', 'password456'),
('AliceSmith', 'password789'),
('BobBrown', 'password321'),
('CharlieBlack', 'password654'),
('DaisyWhite', 'password987'),
('EvaGreen', 'password111'),
('FrankRed', 'password222'),
('GraceBlue', 'password333'),
('HannahYellow', 'password444');

-- הוספת נתונים לטבלת ice_cream
INSERT INTO ice_cream (ice_cream_name, descraption, price_per_ball, price_per_kilo) VALUES
('Vanilla', 'Classic vanilla flavor', 5, 20),
('Chocolate', 'Rich chocolate flavor', 6, 25),
('Strawberry', 'Fresh strawberry flavor', 5, 22),
('Mint', 'Refreshing mint flavor', 6, 23),
('Cookie Dough', 'Delicious cookie dough pieces', 7, 28),
('Pistachio', 'Creamy pistachio flavor', 7, 30),
('Rocky Road', 'Chocolate with marshmallows and nuts', 8, 35),
('Lemon', 'Tangy lemon flavor', 5, 20),
('Coffee', 'Rich coffee flavor', 6, 25),
('Butter Pecan', 'Buttery ice cream with pecans', 7, 28);

-- הוספת נתונים לטבלת orders
INSERT INTO orders (id_customer, date_order, total_price) VALUES
(100, '2024-07-01', 25),
(101, '2024-07-02', 30),
(102, '2024-07-03', 45),
(103, '2024-07-04', 50),
(104, '2024-07-05', 20),
(105, '2024-07-06', 35),
(106, '2024-07-07', 40),
(107, '2024-07-08', 55),
(108, '2024-07-09', 60),
(109, '2024-07-10', 30);
