# Abdulaziz Hamidjonov - Portfolio Website

A minimalist Django portfolio website showcasing AI/ML and Backend development expertise.

## Features

- **Admin Panel Management**: Edit content through Django admin
- **Responsive Design**: Works perfectly on all devices
- **Project Showcase**: Display projects with links and technologies
- **Experience Timeline**: Professional experience and education
- **Contact Form**: Direct contact through the website
- **Social Integration**: Links to GitHub, Telegram, Blog, and Channel

## Technologies Used

- **Backend**: Django 4.2, Python 3.11
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Database**: SQLite (development), PostgreSQL (production)
- **Deployment**: Docker, Nginx
- **Styling**: Custom CSS with modern design principles

## Quick Start

### Local Development

1. **Clone the repository**
   \`\`\`bash
   git clone <your-repo-url>
   cd portfolio
   \`\`\`

2. **Create virtual environment**
   \`\`\`bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   \`\`\`

3. **Install dependencies**
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

4. **Run migrations**
   \`\`\`bash
   python manage.py makemigrations
   python manage.py migrate
   \`\`\`

5. **Create superuser**
   \`\`\`bash
   python manage.py createsuperuser
   \`\`\`

6. **Load initial data (optional)**
   \`\`\`bash
   python manage.py shell
   exec(open('scripts/initial_data.sql').read())
   \`\`\`

7. **Run development server**
   \`\`\`bash
   python manage.py runserver
   \`\`\`

Visit `http://127.0.0.1:8000` to see your portfolio!

### Docker Deployment

1. **Build and run with Docker Compose**
   \`\`\`bash
   docker-compose up --build
   \`\`\`

2. **Access the application**
   - Portfolio: `http://localhost`
   - Admin Panel: `http://localhost/admin`

## Admin Panel

Access the admin panel at `/admin` to manage:

- **About Me**: Personal information, skills, social links
- **Experience**: Work experience, education, certifications
- **Projects**: Portfolio projects with links and technologies
- **Contact Messages**: Messages from the contact form

## Customization

### Adding New Projects

1. Go to Admin Panel → Projects → Add Project
2. Fill in:
   - Title and description
   - Technologies (comma-separated)
   - Project and GitHub links
   - Mark as featured for homepage display

### Updating About Information

1. Go to Admin Panel → About Me
2. Update personal information, skills, and social links
3. Upload profile image and resume

### Managing Experience

1. Go to Admin Panel → Experiences
2. Add work experience, education, or certifications
3. Set order for display sequence

## Deployment

### Production Settings

1. **Environment Variables**
   \`\`\`bash
   export SECRET_KEY='your-secret-key'
   export DEBUG=False
   export ALLOWED_HOSTS='yourdomain.com,www.yourdomain.com'
   export DATABASE_URL='postgresql://user:pass@localhost/dbname'
   \`\`\`

2. **Static Files**
   \`\`\`bash
   python manage.py collectstatic
   \`\`\`

3. **Database Migration**
   \`\`\`bash
   python manage.py migrate
   \`\`\`

### Docker Production

1. **Update docker-compose.prod.yml**
2. **Set environment variables**
3. **Deploy with SSL certificate**

## Performance Features

- **Lazy Loading**: Images load as needed
- **Responsive Images**: Optimized for different screen sizes
- **Minified Assets**: Compressed CSS and JS
- **Caching**: Static file caching with Nginx
- **SEO Optimized**: Meta tags and semantic HTML

## Browser Support

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Contact

- **GitHub**: [abdulaziz-python](https://github.com/abdulaziz-python)
- **Telegram**: [@ablaze_coder](https://t.me/ablaze_coder)
- **Blog**: [@fikrlog_all](https://t.me/fikrlog_all)
- **Channel**: [@pythonnews_uzbekistan](https://t.me/pythonnews_uzbekistan)

---

Built with ❤️ by Abdulaziz Hamidjonov
