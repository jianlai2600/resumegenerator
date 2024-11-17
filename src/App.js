// App.js
import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate, useNavigate } from 'react-router-dom';
import './App.css';

// 基本信息表单
const BasicInfoForm = ({ onNext, formData, setFormData }) => {
  const handleSubmit = (e) => {
    e.preventDefault();
    onNext();
  };

  return (
    <div className="form-container">
      <h2>基本信息</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label>姓名：</label>
          <input
            type="text"
            value={formData.name}
            onChange={(e) => setFormData({...formData, name: e.target.value})}
            required
          />
        </div>
        <div className="form-group">
          <label>年龄：</label>
          <input
            type="number"
            value={formData.age}
            onChange={(e) => setFormData({...formData, age: e.target.value})}
            required
          />
        </div>
        <button type="submit">下一步</button>
      </form>
    </div>
  );
};

// 教育背景表单
const EducationForm = ({ onNext, onBack, formData, setFormData }) => {
  const handleSubmit = (e) => {
    e.preventDefault();
    onNext();
  };

  return (
    <div className="form-container">
      <h2>教育背景</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label>最高学历：</label>
          <select
            value={formData.education}
            onChange={(e) => setFormData({...formData, education: e.target.value})}
            required
          >
            <option value="">请选择</option>
            <option value="高中">高中</option>
            <option value="本科">本科</option>
            <option value="硕士">硕士</option>
            <option value="博士">博士</option>
          </select>
        </div>
        <div className="form-group">
          <label>专业：</label>
          <input
            type="text"
            value={formData.major}
            onChange={(e) => setFormData({...formData, major: e.target.value})}
            required
          />
        </div>
        <div className="button-group">
          <button type="button" onClick={onBack}>上一步</button>
          <button type="submit">下一步</button>
        </div>
      </form>
    </div>
  );
};

// 工作经历表单
const WorkExperienceForm = ({ onNext, onBack, formData, setFormData }) => {
  const handleSubmit = (e) => {
    e.preventDefault();
    onNext();
  };

  return (
    <div className="form-container">
      <h2>工作经历</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label>当前职位：</label>
          <input
            type="text"
            value={formData.currentPosition}
            onChange={(e) => setFormData({...formData, currentPosition: e.target.value})}
            required
          />
        </div>
        <div className="form-group">
          <label>工作年限：</label>
          <input
            type="number"
            value={formData.yearsOfExperience}
            onChange={(e) => setFormData({...formData, yearsOfExperience: e.target.value})}
            required
          />
        </div>
        <div className="button-group">
          <button type="button" onClick={onBack}>上一步</button>
          <button type="submit">完成</button>
        </div>
      </form>
    </div>
  );
};

// 在 App.js 中添加提交函数
const Results = ({ formData }) => {
  const [submitStatus, setSubmitStatus] = useState('');

  const handleSubmit = async () => {
    try {
      const response = await fetch('http://localhost:5000/api/submit', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      const data = await response.json();

      if (response.ok) {
        setSubmitStatus('提交成功！');
      } else {
        setSubmitStatus(`提交失败: ${data.message}`);
      }
    } catch (error) {
      setSubmitStatus(`提交失败: ${error.message}`);
    }
  };

  return (
    <div className="results-container">
      <h2>收集的信息</h2>
      <pre>{JSON.stringify(formData, null, 2)}</pre>
      <button onClick={handleSubmit}>提交问卷</button>
      {submitStatus && <p className={submitStatus.includes('成功') ? 'success' : 'error'}>{submitStatus}</p>}
    </div>
  );
};

// 主应用组件
const App = () => {
  const [formData, setFormData] = useState({
    name: '',
    age: '',
    education: '',
    major: '',
    currentPosition: '',
    yearsOfExperience: '',
  });

  const [step, setStep] = useState(1);

  const nextStep = () => setStep(step + 1);
  const prevStep = () => setStep(step - 1);

  const renderStep = () => {
    switch (step) {
      case 1:
        return (
          <BasicInfoForm
            onNext={nextStep}
            formData={formData}
            setFormData={setFormData}
          />
        );
      case 2:
        return (
          <EducationForm
            onNext={nextStep}
            onBack={prevStep}
            formData={formData}
            setFormData={setFormData}
          />
        );
      case 3:
        return (
          <WorkExperienceForm
            onNext={nextStep}
            onBack={prevStep}
            formData={formData}
            setFormData={setFormData}
          />
        );
      case 4:
        return <Results formData={formData} />;
      default:
        return <Navigate to="/" />;
    }
  };

  return (
    <div className="app">
      <div className="progress-bar">
        <div className="progress" style={{ width: `${(step / 4) * 100}%` }}></div>
      </div>
      {renderStep()}
    </div>
  );
};

export default App;