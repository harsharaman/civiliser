PROMPT = """Extract top 3 technical skills required for a job from a given job description.

Input: {job_description}

Output: A list of 3 technical skills (tools, technologies, or methodologies) that are most relevant to the job.

Instructions:

1. Parse the job description to identify the job title and responsibilities.
2. Extract keywords and phrases related to technical skills from the job description.
3. Filter out non-technical skills and generic terms (e.g., communication skills, problem-solving skills).
4. Rank the extracted technical skills by their frequency and relevance to the job responsibilities.
5. Return the top 3 technical skills as a list.

Format: [Skill 1, Skill 2, Skill 3]

Example input:
Job brief

We are seeking a highly skilled Hardware Engineer to join our team and contribute to the design, development, and testing of our hardware products. As a Hardware Engineer, you will be responsible for designing and developing hardware components, testing and validating hardware prototypes, and ensuring that our hardware products meet the highest standards of quality and reliability.

Responsibilities

    Design and develop hardware components, including circuit boards, microcontrollers, and sensors
    Test and validate hardware prototypes to ensure they meet design specifications
    Collaborate with cross-functional teams to identify and prioritize project requirements
    Develop and maintain technical documentation for hardware products
    Troubleshoot and resolve hardware issues and bugs
    Participate in the development of test plans and procedures for hardware products
    Stay up-to-date with industry trends and emerging technologies in hardware engineering

Requirements and skills

    Proven work experience as a Hardware Engineer or similar role
    Strong proficiency in electronics and circuit design
    Experience with hardware development tools (e.g., CAD, simulation software)
    Strong understanding of electronics and circuit principles
    Excellent problem-solving and analytical skills
    Great communication and collaboration skills
    Relevant training and/or certifications in hardware engineering (e.g., PCB design, microcontroller programming)

Expected output: A list of 3 technical skills, e.g., [CAD, Simulation Software, PCB Design]

Please respond with the extracted technical skills."

"""