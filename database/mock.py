from schemas.cv import CV, Contact, SkillSet, Experience, Education, Language, Interest

cv = CV(
    contact=Contact(
        name="Giannis Bratias",
        address="Athens, Greece",
        phone="+30 697 5709995",
        email="gbratias@gmail.com",
        linkedin="https://www.linkedin.com/in/giannis-bratias-974a31178/"
    ),
    skills=SkillSet(
        highlights=[
            "Detail Oriented", "Quick Learner", "Autonomous", "Accountability/Ownership",
            "Problem Solving", "Team Oriented", "Agile"
        ],
        technical=[
            "Python", "Django/Rest framework", "Version Control/Git", "Nginx/Gunicorn",
            "Linux/CLI", "Docker", "Celery", "Redis", "AWS infrastructure"
        ]
    ),
    languages=Language(root=["Greek", "English", "Albanian"]),
    experience=[
        Experience(
            title="Backend Software Engineer",
            company="Grapevine",
            start="07/2022",
            end="Present",
            bullets=[
                "Designed and implemented highly efficient targeted systems, such as parsers with acyclic graph validation using NetworkX.",
                "Managed Celery/Redis crises by diagnosing issues and manually clearing stuck tasks to prevent memory overflows.",
                "Built REST APIs using Django Rest Framework.",
                "Handled complex deployment scenarios including conflict resolution and rollback.",
                "Developed decision processors for mismatch handling with error/warning notifications.",
                "Collaborated with frontend and product teams for API design and feature development.",
                "Integrated platforms like Zapier (REST hooks) and Microsoft Entra ID (SCIM sync)."
            ]
        ),
        Experience(
            title="Web Developer",
            company="Radial",
            start="03/2021",
            end="07/2022",
            bullets=[
                "Developed Django Oscar e-commerce and Wagtail CMS websites.",
                "Managed deployment configurations and server setup.",
                "Integrated 3rd-party APIs and external services.",
                "Implemented a backordering system.",
                "Improved dynamic search filters.",
                "Automated tasks using Makefile and Fabric."
            ]
        ),
        Experience(
            title="Web Developer (Internship)",
            company="Just In Time",
            start="09/2020",
            end="11/2020",
            bullets=[
                "Frontend modifications in web development projects.",
                "Web design and content management using WordPress CMS."
            ]
        )
    ],
    education=[
        Education(
            degree="Bachelor of Science: Mechanical Engineering",
            institution="Technological Educational Institute of Piraeus",
            location="Athens, Greece"
        )
    ],
    interests=Interest(root=["Hiking", "Working out", "Cooking", "Biking", "Building computers"])
)
