"""
generate_samples.py - Creates dummy resume files for testing

Run this once to populate the resumes/ folder:
    python generate_samples.py

It'll create 10 resumes - 6 txt, 2 pdf, 2 docx.
"""

import os
import textwrap


# All the resume data - Indian names, cities, colleges, companies
RESUMES = [
    {
        "filename": "resume_arjun_sharma.txt",
        "content": textwrap.dedent("""\
            ARJUN SHARMA
            Email: arjun.sharma@email.com | Phone: +91 98765 43210
            LinkedIn: linkedin.com/in/arjunsharma | GitHub: github.com/arjunsharma
            Location: Bangalore, Karnataka

            PROFESSIONAL SUMMARY
            Senior Software Engineer with 5 years of experience specializing in
            Python, Django, and cloud infrastructure. Passionate about building
            scalable backend systems and automating deployment pipelines.

            SKILLS
            Languages: Python, SQL, Bash, JavaScript
            Frameworks: Django, Flask, FastAPI, Celery
            Cloud & DevOps: AWS (EC2, S3, Lambda, RDS), Docker, Terraform
            Databases: PostgreSQL, Redis, MongoDB
            Tools: Git, Jenkins, Jira, Confluence

            WORK EXPERIENCE

            Senior Software Engineer — Flipkart, Bangalore, Karnataka
            June 2021 – Present
            • Led migration of monolithic Django application to microservices architecture
            • Designed and implemented RESTful APIs serving 10M+ requests/day
            • Reduced AWS infrastructure costs by 30% through resource optimization
            • Mentored 3 junior developers in Python best practices and code review

            Software Engineer — Zoho Corporation, Chennai, Tamil Nadu
            Jan 2019 – May 2021
            • Built data ingestion pipelines processing 500GB of daily logs using Python
            • Developed automated testing suite achieving 92% code coverage
            • Implemented CI/CD pipeline using Jenkins and Docker
            • Collaborated with data science team on ML model deployment

            EDUCATION
            B.Tech Computer Science — IIT Bombay (2018)

            CERTIFICATIONS
            • AWS Certified Solutions Architect – Associate
            • Python Institute PCPP – Certified Professional in Python Programming
        """),
    },
    {
        "filename": "resume_priya_nair.txt",
        "content": textwrap.dedent("""\
            PRIYA NAIR
            Email: priya.nair@email.com | Phone: +91 87654 32109
            LinkedIn: linkedin.com/in/priyanair
            Location: Hyderabad, Telangana

            PROFESSIONAL SUMMARY
            Staff Software Engineer with 8 years of experience in enterprise Java
            development, distributed systems, and container orchestration.
            Proven track record of delivering high-availability services at scale.

            SKILLS
            Languages: Java, Kotlin, Go, Python
            Frameworks: Spring Boot, Spring Cloud, Hibernate, gRPC
            Cloud & DevOps: Kubernetes, Docker, AWS, GCP, Helm, ArgoCD
            Databases: MySQL, PostgreSQL, Cassandra, Elasticsearch
            Tools: Git, Gradle, Maven, Prometheus, Grafana

            WORK EXPERIENCE

            Staff Software Engineer — Google India, Hyderabad, Telangana
            Mar 2020 – Present
            • Architected event-driven microservices platform handling 50K events/sec
            • Led Kubernetes migration for 40+ services with zero downtime
            • Designed circuit-breaker patterns reducing cascading failures by 90%
            • Established SRE practices including SLOs, error budgets, and on-call

            Senior Software Engineer — Paytm, Noida, Uttar Pradesh
            Jul 2017 – Feb 2020
            • Built real-time payment processing system using Spring Boot and Kafka
            • Implemented OAuth2/OIDC authentication for 2M+ users
            • Optimized database queries reducing p99 latency from 800ms to 120ms
            • Conducted technical interviews and onboarded new team members

            Software Engineer — Wipro Technologies, Bangalore, Karnataka
            Jun 2015 – Jun 2017
            • Developed e-commerce backend using Java and Spring MVC
            • Integrated third-party payment gateways (Razorpay, PayU)
            • Automated deployment workflows using Jenkins and Ansible

            EDUCATION
            M.Tech Computer Science — IIT Madras (2015)
            B.Tech Computer Science — NIT Trichy (2013)

            CERTIFICATIONS
            • Certified Kubernetes Administrator (CKA)
            • Oracle Certified Professional Java SE 17 Developer
        """),
    },
    {
        "filename": "resume_rahul_verma.pdf",
        "content": textwrap.dedent("""\
            RAHUL VERMA
            Email: rahul.verma@email.com | Phone: +91 76543 21098
            LinkedIn: linkedin.com/in/rahulverma | GitHub: github.com/rahulverma
            Location: Mumbai, Maharashtra

            PROFESSIONAL SUMMARY
            Machine Learning Engineer with 3 years of experience building and
            deploying production ML systems. Strong foundation in Python,
            deep learning frameworks, and MLOps best practices.

            SKILLS
            Languages: Python, R, SQL, C++
            ML/AI: TensorFlow, PyTorch, scikit-learn, Hugging Face Transformers
            Data: Pandas, NumPy, Spark, Airflow, dbt
            Cloud & MLOps: AWS SageMaker, MLflow, Kubeflow, Docker
            Tools: Git, Jupyter, Weights & Biases, DVC

            WORK EXPERIENCE

            Machine Learning Engineer — Jio AI Labs, Mumbai, Maharashtra
            Aug 2022 – Present
            • Developed NLP pipeline for resume parsing using BERT-based models
            • Built real-time recommendation engine serving 5M+ users with <50ms latency
            • Designed A/B testing framework for model evaluation in production
            • Reduced model training time by 60% through distributed training on GPUs

            Data Scientist — Fractal Analytics, Pune, Maharashtra
            May 2021 – Jul 2022
            • Built customer churn prediction model achieving 94% accuracy using Python
            • Created automated feature engineering pipeline using Pandas and scikit-learn
            • Deployed models as REST APIs using FastAPI and Docker
            • Conducted statistical analysis and presented findings to C-suite

            ML Research Intern — IISc Bangalore, Bangalore, Karnataka
            Jun 2020 – Apr 2021
            • Researched transformer architectures for text classification
            • Published paper on efficient fine-tuning of large language models
            • Contributed to open-source TensorFlow model garden

            EDUCATION
            M.Tech Data Science — IIT Delhi (2021)
            B.Tech Computer Science — BITS Pilani (2019)

            PUBLICATIONS
            • "Efficient Fine-Tuning Strategies for LLMs" — NeurIPS Workshop 2021
        """),
    },
    {
        "filename": "resume_sneha_iyer.docx",
        "content": textwrap.dedent("""\
            SNEHA IYER
            Email: sneha.iyer@email.com | Phone: +91 65432 10987
            LinkedIn: linkedin.com/in/snehaiyer | Portfolio: snehaiyer.dev
            Location: Pune, Maharashtra

            PROFESSIONAL SUMMARY
            Full-Stack Developer with 6 years of experience building modern web
            applications. Expert in JavaScript ecosystem with deep knowledge of
            React, Node.js, and cloud-native architectures.

            SKILLS
            Languages: JavaScript, TypeScript, HTML, CSS, Python
            Frontend: React, Next.js, Redux, Tailwind CSS, Storybook
            Backend: Node.js, Express, NestJS, GraphQL, REST
            Databases: PostgreSQL, MongoDB, Redis, DynamoDB
            Cloud & DevOps: AWS, Vercel, Docker, GitHub Actions, Terraform
            Tools: Git, Figma, Webpack, Vite, Jest, Cypress

            WORK EXPERIENCE

            Senior Full-Stack Developer — Razorpay, Bangalore, Karnataka
            Apr 2021 – Present
            • Led development of SaaS platform used by 200K+ businesses
            • Built server-side rendered app using Next.js improving SEO scores by 45%
            • Implemented real-time collaboration features using WebSockets
            • Reduced page load time by 50% through code splitting and lazy loading

            Full-Stack Developer — Freshworks, Chennai, Tamil Nadu
            Sep 2018 – Mar 2021
            • Developed React-based dashboard for analytics platform
            • Built Node.js microservices for user management and notifications
            • Designed and implemented GraphQL API layer for mobile and web clients
            • Set up CI/CD pipelines using GitHub Actions and Docker

            Junior Developer — TCS Digital, Mumbai, Maharashtra
            Jun 2017 – Aug 2018
            • Built responsive websites using React and CSS Grid
            • Developed REST APIs using Express.js and MongoDB
            • Participated in agile sprints and daily standups

            EDUCATION
            B.Tech Computer Science — COEP Pune (2017)

            CERTIFICATIONS
            • AWS Certified Developer – Associate
            • Meta Front-End Developer Professional Certificate
        """),
    },
    {
        "filename": "resume_vikram_reddy.txt",
        "content": textwrap.dedent("""\
            VIKRAM REDDY
            Email: vikram.reddy@email.com | Phone: +91 54321 09876
            LinkedIn: linkedin.com/in/vikramreddy | GitHub: github.com/vikramreddy
            Location: Hyderabad, Telangana

            PROFESSIONAL SUMMARY
            Data Engineer with 4 years of experience designing and maintaining
            large-scale data platforms. Skilled in Python, Apache Spark, and
            modern data stack technologies.

            SKILLS
            Languages: Python, Scala, SQL, Java
            Big Data: Apache Spark, Kafka, Flink, Hadoop
            Data Tools: Airflow, dbt, Snowflake, BigQuery, Redshift
            Cloud: AWS (EMR, Glue, S3, Kinesis), GCP (Dataflow, Pub/Sub)
            Databases: PostgreSQL, Cassandra, HBase, Delta Lake
            Tools: Git, Docker, Kubernetes, Terraform, Great Expectations

            WORK EXPERIENCE

            Senior Data Engineer — Amazon India, Hyderabad, Telangana
            Jan 2022 – Present
            • Architected real-time streaming pipeline processing 2B events/day using Kafka and Spark
            • Led migration from Hadoop to Snowflake reducing query times by 75%
            • Built data quality monitoring framework using Great Expectations and Python
            • Designed dimensional data models serving analytics for 500+ internal users

            Data Engineer — Mu Sigma, Bangalore, Karnataka
            Jun 2020 – Dec 2021
            • Built ETL pipelines processing 5TB of daily sales data using Python and Spark
            • Implemented data lake architecture on AWS S3 with Delta Lake format
            • Created dbt models for business-critical KPI dashboards
            • Automated data pipeline orchestration using Apache Airflow

            EDUCATION
            M.Tech Computer Science — IIIT Hyderabad (2020)
            B.Tech Information Technology — NIT Warangal (2018)

            CERTIFICATIONS
            • Databricks Certified Data Engineer Professional
            • AWS Certified Data Analytics – Specialty
        """),
    },
    {
        "filename": "resume_meera_krishnan.txt",
        "content": textwrap.dedent("""\
            MEERA KRISHNAN
            Email: meera.krishnan@email.com | Phone: +91 43210 98765
            LinkedIn: linkedin.com/in/meerakrishnan
            Location: Chennai, Tamil Nadu

            PROFESSIONAL SUMMARY
            Embedded Systems Engineer with 7 years of experience in firmware
            development, real-time operating systems, and hardware-software
            integration. Strong background in C++ and safety-critical systems.

            SKILLS
            Languages: C++, C, Python, Assembly (ARM, x86)
            RTOS: FreeRTOS, Zephyr, VxWorks, QNX
            Protocols: CAN, SPI, I2C, UART, Ethernet, MQTT
            Tools: JTAG, Oscilloscope, Logic Analyzer, Valgrind
            Hardware: ARM Cortex-M/A, STM32, ESP32, Raspberry Pi
            Development: Git, CMake, GDB, CI/CD (GitLab CI)

            WORK EXPERIENCE

            Senior Embedded Engineer — Tata Elxsi, Bangalore, Karnataka
            May 2020 – Present
            • Designed ADAS sensor fusion module for autonomous vehicle platform
            • Developed real-time control software on FreeRTOS meeting <1ms deadlines
            • Implemented CAN bus communication stack for vehicle ECU network
            • Led team of 4 engineers in MISRA C++ compliant firmware development

            Embedded Software Engineer — Robert Bosch India, Coimbatore, Tamil Nadu
            Jul 2017 – Apr 2020
            • Built firmware for fleet of 10K+ IoT sensor devices using C++ and Zephyr
            • Developed OTA firmware update system with rollback capability
            • Optimized power management achieving 2-year battery life on coin cell
            • Created hardware abstraction layer for multi-platform support

            Junior Firmware Developer — HCL Technologies, Noida, Uttar Pradesh
            Jun 2016 – Jun 2017
            • Developed firmware for medical monitoring devices
            • Implemented IEC 62304 compliant software development lifecycle
            • Wrote unit tests for safety-critical code paths

            EDUCATION
            M.Tech VLSI Design — IIT Kharagpur (2016)
            B.Tech Electronics & Communication — Anna University, Chennai (2014)

            CERTIFICATIONS
            • ISTQB Certified Tester – Foundation Level
            • ARM Accredited Engineer
        """),
    },
    {
        "filename": "resume_ankit_patel.docx",
        "content": textwrap.dedent("""\
            ANKIT PATEL
            Email: ankit.patel@email.com | Phone: +91 32109 87654
            LinkedIn: linkedin.com/in/ankitpatel | GitHub: github.com/ankitpatel
            Location: Ahmedabad, Gujarat

            PROFESSIONAL SUMMARY
            Backend Developer with 2 years of experience building RESTful APIs
            and microservices using Python and FastAPI. Eager learner with strong
            fundamentals in database design and clean code practices.

            SKILLS
            Languages: Python, SQL, TypeScript, Go
            Frameworks: FastAPI, SQLAlchemy, Pydantic, Alembic
            Databases: PostgreSQL, Redis, SQLite, MongoDB
            Cloud & DevOps: AWS (ECS, RDS, SQS), Docker, GitHub Actions
            Tools: Git, Postman, pgAdmin, VS Code, Pytest
            Concepts: REST API Design, TDD, SOLID Principles, Clean Architecture

            WORK EXPERIENCE

            Backend Developer — CRED, Bangalore, Karnataka
            Aug 2023 – Present
            • Built RESTful API platform using Python and FastAPI serving 100K daily users
            • Designed PostgreSQL schema for multi-tenant SaaS application
            • Implemented async task processing using Celery and Redis
            • Wrote comprehensive test suite with 95% coverage using Pytest
            • Set up monitoring and alerting using Prometheus and PagerDuty

            Software Engineering Intern — Infosys, Mysore, Karnataka
            Jan 2023 – Jul 2023
            • Developed CRUD APIs for internal tools using FastAPI and SQLAlchemy
            • Built automated database migration pipeline using Alembic
            • Created Python scripts for data migration from legacy MySQL to PostgreSQL
            • Participated in code reviews and sprint planning

            EDUCATION
            B.Tech Computer Science — DA-IICT Gandhinagar (2023)

            PROJECTS
            • Open-source Python CLI for API load testing (500+ GitHub stars)
            • Personal blog platform built with FastAPI and HTMX
        """),
    },
    {
        "filename": "resume_kavita_singh.txt",
        "content": textwrap.dedent("""\
            KAVITA SINGH
            Email: kavita.singh@email.com | Phone: +91 21098 76543
            LinkedIn: linkedin.com/in/kavitasingh
            Location: Jaipur, Rajasthan

            PROFESSIONAL SUMMARY
            Full-Stack Developer with 5 years of experience specializing in
            Ruby on Rails, GraphQL, and modern frontend technologies.
            Passionate about developer experience and API design.

            SKILLS
            Languages: Ruby, JavaScript, TypeScript, SQL, Python
            Backend: Ruby on Rails, Sinatra, Sidekiq, GraphQL (graphql-ruby)
            Frontend: React, Stimulus, Hotwire (Turbo + Stimulus), Tailwind CSS
            Databases: PostgreSQL, Redis, Elasticsearch
            Cloud & DevOps: Heroku, AWS, Docker, CircleCI, Datadog
            Tools: Git, RSpec, Minitest, Rubocop, Webpack

            WORK EXPERIENCE

            Senior Developer — Zerodha, Bangalore, Karnataka
            Feb 2022 – Present
            • Lead developer on Rails 7 application serving 50K+ subscribers
            • Migrated REST API to GraphQL reducing frontend data fetching by 60%
            • Implemented real-time notifications using Hotwire and ActionCable
            • Improved deployment pipeline reducing release cycle from 1 week to daily

            Full-Stack Developer — Hasura, Bangalore, Karnataka
            Jun 2019 – Jan 2022
            • Built multi-tenant e-commerce platform using Ruby on Rails
            • Developed custom payment integration with Razorpay and PayU
            • Created admin dashboard using React and GraphQL
            • Mentored 2 junior developers and conducted code reviews

            Junior Developer — Mindtree, Pune, Maharashtra
            May 2018 – May 2019
            • Developed features for content management system in Rails
            • Wrote RSpec tests maintaining 90% code coverage
            • Built responsive UI components using Stimulus and Tailwind CSS

            EDUCATION
            B.Tech Computer Science — MNIT Jaipur (2018)

            CERTIFICATIONS
            • AWS Certified Cloud Practitioner
        """),
    },
    {
        "filename": "resume_deepak_gupta.txt",
        "content": textwrap.dedent("""\
            DEEPAK GUPTA
            Email: deepak.gupta@email.com | Phone: +91 10987 65432
            LinkedIn: linkedin.com/in/deepakgupta | GitHub: github.com/deepakgupta
            Location: Delhi NCR

            PROFESSIONAL SUMMARY
            DevOps Engineer with 6 years of experience in CI/CD, infrastructure
            automation, and cloud architecture. Expert in Python scripting,
            Docker containerization, and Infrastructure as Code.

            SKILLS
            Languages: Python, Bash, Go, YAML, HCL
            CI/CD: Jenkins, GitHub Actions, GitLab CI, ArgoCD, Tekton
            Containers: Docker, Kubernetes, Helm, Istio, Podman
            Cloud: AWS (EKS, ECS, Lambda, CloudFormation), Azure, GCP
            IaC: Terraform, Ansible, Pulumi, CloudFormation
            Monitoring: Prometheus, Grafana, ELK Stack, Datadog, PagerDuty
            Tools: Git, Vault, Consul, Nexus, SonarQube

            WORK EXPERIENCE

            Senior DevOps Engineer — PhonePe, Bangalore, Karnataka
            Oct 2021 – Present
            • Architected Kubernetes platform hosting 100+ microservices on AWS EKS
            • Built zero-downtime deployment pipeline using ArgoCD and Helm
            • Developed Python-based infrastructure automation reducing provisioning from days to minutes
            • Implemented secrets management using HashiCorp Vault
            • Established SRE practices achieving 99.95% uptime SLA

            DevOps Engineer — Ola Cabs, Bangalore, Karnataka
            Mar 2019 – Sep 2021
            • Migrated legacy applications to Docker containers and Kubernetes
            • Automated infrastructure provisioning using Terraform and Ansible
            • Built CI/CD pipelines for 30+ repositories using Jenkins and GitHub Actions
            • Created Python monitoring scripts integrated with Prometheus and Grafana

            Systems Administrator — Tech Mahindra, Noida, Uttar Pradesh
            Jul 2017 – Feb 2019
            • Managed Linux server fleet of 200+ servers
            • Automated routine tasks using Python and Bash scripts
            • Implemented centralized logging with ELK Stack
            • Configured network security and firewall rules

            EDUCATION
            B.Tech Information Technology — DTU Delhi (2017)

            CERTIFICATIONS
            • AWS Certified DevOps Engineer – Professional
            • Certified Kubernetes Administrator (CKA)
            • HashiCorp Certified Terraform Associate
        """),
    },
    {
        "filename": "resume_pooja_deshmukh.pdf",
        "content": textwrap.dedent("""\
            POOJA DESHMUKH
            Email: pooja.deshmukh@email.com | Phone: +91 99887 76655
            LinkedIn: linkedin.com/in/poojadeshmukh | GitHub: github.com/poojadeshmukh
            Location: Pune, Maharashtra

            PROFESSIONAL SUMMARY
            Backend Engineer with 4 years of experience building high-performance
            distributed systems using Go. Passionate about microservices
            architecture, gRPC, and system design.

            SKILLS
            Languages: Go, Python, Rust, SQL, Protobuf
            Frameworks: Gin, Echo, gRPC-Go, NATS, Temporal
            Infrastructure: Kubernetes, Docker, Istio, Envoy, Consul
            Databases: PostgreSQL, CockroachDB, Redis, etcd, ScyllaDB
            Cloud: GCP (GKE, Cloud Run, Pub/Sub, Spanner), AWS
            Tools: Git, Buf, Wire, GoReleaser, Prometheus, Jaeger

            WORK EXPERIENCE

            Backend Engineer — Swiggy, Bangalore, Karnataka
            May 2022 – Present
            • Built high-throughput order processing system in Go handling 100K req/s
            • Designed gRPC service mesh with Istio for inter-service communication
            • Implemented distributed tracing using OpenTelemetry and Jaeger
            • Created Go SDK for internal platform adopted by 15 engineering teams

            Software Engineer — Directi (Media.net), Mumbai, Maharashtra
            Mar 2021 – Apr 2022
            • Developed event-driven microservices using Go and NATS messaging
            • Built service discovery and configuration management using Consul
            • Implemented rate limiting and circuit breaking with custom Go middleware
            • Optimized garbage collection reducing p99 latency spikes by 40%

            Junior Developer — ThoughtWorks India, Pune, Maharashtra
            Jun 2020 – Feb 2021
            • Built REST APIs in Go using the Gin framework
            • Wrote integration tests and set up CI/CD with GitHub Actions
            • Contributed to open-source Go libraries for JSON processing

            EDUCATION
            B.Tech Computer Science — VJTI Mumbai (2020)

            CERTIFICATIONS
            • Google Cloud Professional Cloud Developer
            • Go Developer Certification (by Ardan Labs)
        """),
    },
]


# --- file creators for each format ---

def create_txt(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"  [OK] {path}")


def create_pdf(path, content):
    """Generate a basic PDF with the resume text."""
    from reportlab.lib.pagesizes import LETTER
    from reportlab.lib.units import inch
    from reportlab.pdfgen import canvas

    c = canvas.Canvas(path, pagesize=LETTER)
    width, height = LETTER
    margin = 1 * inch
    y = height - margin

    for line in content.splitlines():
        if y < margin:
            c.showPage()
            y = height - margin
        c.setFont("Helvetica", 10)
        c.drawString(margin, y, line[:90])  # truncate long lines
        y -= 14

    c.save()
    print(f"  [OK] {path}")


def create_docx(path, content):
    """Generate a DOCX file with the resume text."""
    from docx import Document
    doc = Document()
    for line in content.splitlines():
        doc.add_paragraph(line)
    doc.save(path)
    print(f"  [OK] {path}")


CREATORS = {
    ".txt": create_txt,
    ".pdf": create_pdf,
    ".docx": create_docx,
}


def main():
    out_dir = os.path.join(os.path.dirname(__file__), "resumes")
    os.makedirs(out_dir, exist_ok=True)

    print(f"Generating {len(RESUMES)} sample resumes in '{out_dir}/':\n")

    for resume in RESUMES:
        filename = resume["filename"]
        ext = os.path.splitext(filename)[1].lower()
        filepath = os.path.join(out_dir, filename)

        creator = CREATORS.get(ext)
        if creator is None:
            print(f"  [SKIP] Unsupported format: {filename}")
            continue
        creator(filepath, resume["content"])

    # make sure the output directory exists too
    output_dir = os.path.join(os.path.dirname(__file__), "output")
    os.makedirs(output_dir, exist_ok=True)
    print(f"\nCreated output directory: {output_dir}/")
    print("\nDone! All sample resumes generated.")


if __name__ == "__main__":
    main()
