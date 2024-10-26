import React, { useState } from 'react';
import { Container, Button, Form, ProgressBar } from 'react-bootstrap';

function App() {
    const [step, setStep] = useState(1);  // Current step
    const [name, setName] = useState('');
    const [contact, setContact] = useState('');
    const [education, setEducation] = useState('');
    const [experiences, setExperiences] = useState([]);
    const [skills, setSkills] = useState([]);
    const [experienceInput, setExperienceInput] = useState('');
    const [skillInput, setSkillInput] = useState('');
    const [resumeGenerated, setResumeGenerated] = useState(false);

    // Handle next button click
    const handleNext = () => {
        if (step === 5) {
            setResumeGenerated(true);  // Generate resume on the last step
        } else {
            setStep(step + 1);
        }
    };

    // Handle back button click
    const handleBack = () => {
        setStep(step - 1);
    };

    // Handle return to homepage
    const handleReturnToHome = () => {
        setStep(1);
        setResumeGenerated(false);
        setName('');
        setContact('');
        setEducation('');
        setExperiences([]);
        setSkills([]);
    };

    const addExperience = () => {
        setExperiences([...experiences, experienceInput]);
        setExperienceInput('');
    };

    const addSkill = () => {
        setSkills([...skills, skillInput]);
        setSkillInput('');
    };

    const renderFormContent = () => {
        switch (step) {
            case 1:
                return (
                    <>
                        <h4>Welcome! Please tell us your name</h4>
                        <Form.Control
                            type="text"
                            placeholder="Enter your name"
                            value={name}
                            onChange={(e) => setName(e.target.value)}
                        />
                    </>
                );
            case 2:
                return (
                    <>
                        <h4>Please provide your contact information</h4>
                        <Form.Control
                            type="text"
                            placeholder="Enter your contact information"
                            value={contact}
                            onChange={(e) => setContact(e.target.value)}
                        />
                    </>
                );
            case 3:
                return (
                    <>
                        <h4>Please enter your educational background</h4>
                        <Form.Control
                            type="text"
                            placeholder="Enter your educational background"
                            value={education}
                            onChange={(e) => setEducation(e.target.value)}
                        />
                    </>
                );
            case 4:
                return (
                    <>
                        <h4>Please add your work experiences</h4>
                        <Form.Control
                            type="text"
                            placeholder="Enter work experience"
                            value={experienceInput}
                            onChange={(e) => setExperienceInput(e.target.value)}
                        />
                        <Button variant="primary" onClick={addExperience}>Add Experience</Button>
                        <ul>
                            {experiences.map((exp, idx) => <li key={idx}>{exp}</li>)}
                        </ul>
                    </>
                );
            case 5:
                return (
                    <>
                        <h4>Please add your skills</h4>
                        <Form.Control
                            type="text"
                            placeholder="Enter skill"
                            value={skillInput}
                            onChange={(e) => setSkillInput(e.target.value)}
                        />
                        <Button variant="primary" onClick={addSkill}>Add Skill</Button>
                        <ul>
                            {skills.map((skill, idx) => <li key={idx}>{skill}</li>)}
                        </ul>
                    </>
                );
            default:
                return null;
        }
    };

    const renderResume = () => (
    <div className="resume-preview">
        <h3>Your Resume</h3>
        <iframe
            src="http://127.0.0.1:5000/generate_resume"
            width="100%"
            height="500px"
            title="Resume PDF"
        ></iframe>
        <Button variant="primary" href="http://127.0.0.1:5000/generate_resume" download className="mt-3">
            Download Resume
        </Button>
    </div>
    );

    return (
        <Container className="mt-5">
            <h2 className="text-center mb-4">Resume Generator</h2>
            <ProgressBar now={(step / 5) * 100} label={`Step ${step} / 5`} className="mb-4" />
            {resumeGenerated ? (
                renderResume()
            ) : (
                <Form>
                    {renderFormContent()}
                    <div className="d-flex justify-content-between mt-4">
                        {step > 1 && <Button variant="secondary" onClick={handleBack}>Back</Button>}
                        <Button variant="primary" onClick={handleNext}>{step === 5 ? 'Generate Resume' : 'Next'}</Button>
                    </div>
                </Form>
            )}
        </Container>
    );
}

export default App;
