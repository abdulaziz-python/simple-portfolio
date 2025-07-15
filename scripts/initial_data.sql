-- Create initial About record
INSERT INTO main_about (
    name, 
    title, 
    description, 
    github_username, 
    telegram_username, 
    blog_handle, 
    channel_handle, 
    skills,
    created_at,
    updated_at
) VALUES (
    'Abdulaziz Hamidjonov',
    'AI/ML & Backend Developer',
    'Passionate AI/ML and Backend Developer specializing in Python, Django, and Telegram Bot development. Experienced in building scalable web applications, machine learning solutions, and automated systems. I love creating innovative solutions that solve real-world problems.',
    'abdulaziz-python',
    'ablaze_coder',
    '@fikrlog_all',
    '@pythonnews_uzbekistan',
    'Python, Django, DRF, TensorFlow, Aiogram, Telebot, PostgreSQL, Git, Docker, AI/ML, Payment Systems, Machine Learning, Deep Learning, Data Analysis',
    datetime('now'),
    datetime('now')
);

-- Sample Experience records
INSERT INTO main_experience (
    title,
    company_or_institution,
    location,
    start_date,
    end_date,
    is_current,
    description,
    experience_type,
    "order"
) VALUES 
(
    'Senior Backend Developer',
    'Tech Solutions Inc.',
    'Tashkent, Uzbekistan',
    '2023-01-01',
    NULL,
    1,
    'Leading backend development projects using Django and PostgreSQL. Developed scalable APIs, implemented payment systems, and created automated Telegram bots for business processes. Mentored junior developers and established best practices for code quality.',
    'work',
    1
),
(
    'AI/ML Developer',
    'DataTech Solutions',
    'Remote',
    '2022-03-01',
    '2022-12-31',
    0,
    'Developed machine learning models using TensorFlow and Python. Created data analysis pipelines, implemented recommendation systems, and built predictive models for business intelligence. Worked with large datasets and optimized model performance.',
    'work',
    2
),
(
    'Python Developer',
    'StartupHub',
    'Tashkent, Uzbekistan',
    '2021-06-01',
    '2022-02-28',
    0,
    'Built web applications using Django framework. Developed REST APIs, integrated third-party services, and created automated testing suites. Collaborated with frontend teams to deliver full-stack solutions.',
    'work',
    3
),
(
    'Computer Science Degree',
    'Tashkent University of Information Technologies',
    'Tashkent, Uzbekistan',
    '2019-09-01',
    '2023-06-30',
    0,
    'Bachelor''s degree in Computer Science with focus on Software Engineering and Artificial Intelligence. Completed projects in machine learning, web development, and database design. Graduated with honors.',
    'education',
    1
);

-- Sample Project records
INSERT INTO main_project (
    title,
    description,
    frameworks,
    project_link,
    github_link,
    is_featured,
    "order",
    created_at,
    updated_at
) VALUES 
(
    'AI-Powered Telegram Bot',
    'An intelligent Telegram bot that uses natural language processing to provide automated customer support. Features include sentiment analysis, automated responses, and integration with business systems. Built with aiogram and TensorFlow.',
    'Python, Aiogram, TensorFlow, PostgreSQL, Docker',
    'https://t.me/your_bot',
    'https://github.com/abdulaziz-python/ai-telegram-bot',
    1,
    1,
    datetime('now'),
    datetime('now')
),
(
    'E-commerce Payment System',
    'A secure payment processing system for e-commerce platforms. Supports multiple payment gateways, handles transactions securely, and provides detailed analytics. Built with Django and integrated with popular payment providers.',
    'Django, DRF, PostgreSQL, Redis, Celery',
    'https://payment-demo.example.com',
    'https://github.com/abdulaziz-python/payment-system',
    1,
    2,
    datetime('now'),
    datetime('now')
),
(
    'Machine Learning Data Pipeline',
    'An automated data processing pipeline for machine learning workflows. Features data ingestion, preprocessing, model training, and deployment automation. Includes monitoring and alerting capabilities.',
    'Python, TensorFlow, Apache Airflow, Docker, Kubernetes',
    NULL,
    'https://github.com/abdulaziz-python/ml-pipeline',
    1,
    3,
    datetime('now'),
    datetime('now')
),
(
    'Django REST API Template',
    'A production-ready Django REST API template with authentication, permissions, testing, and documentation. Includes Docker configuration, CI/CD setup, and best practices for scalable API development.',
    'Django, DRF, PostgreSQL, Docker, GitHub Actions',
    'https://api-template.example.com',
    'https://github.com/abdulaziz-python/django-api-template',
    0,
    4,
    datetime('now'),
    datetime('now')
),
(
    'Telegram Channel Analytics Bot',
    'A comprehensive analytics bot for Telegram channels that tracks engagement, subscriber growth, and content performance. Provides detailed reports and insights for channel administrators.',
    'Python, Telebot, SQLite, Matplotlib, Pandas',
    NULL,
    'https://github.com/abdulaziz-python/channel-analytics-bot',
    0,
    5,
    datetime('now'),
    datetime('now')
);
