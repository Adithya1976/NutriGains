import React, { useState } from 'react';
import './faq.css';
import Navbar from '../NavBar/navBar.js';  // Adjust the path as necessary

const questionsAnswers = [
    {
      question: "What is Nutrigains?",
      answer: "Nutrigains is a personalized meal planning and nutrition management platform available exclusively on the web. It's designed to help users make informed dietary choices and achieve their health and wellness goals through features such as meal recommendations, nutritional tracking, recipe suggestions, and more."
    },
    {
      question: "How does Nutrigains work?",
      answer: "Nutrigains works by utilizing user-provided information such as age, gender, weight, height, and activity level to calculate personalized nutritional needs. It then offers meal recommendations, tracks nutritional intake, and provides access to a database of recipes tailored to individual preferences and dietary requirements, all within a web-based interface."
    },
    {
      question: "How are my macro goals calculated in Nutrigains?",
      answer: "In Nutrigains, daily goal values for essential nutrients such as calories, proteins, carbohydrates, and fats are calculated using the Mifflin St. Jeor equation. This equation considers user attributes like weight, height, and gender, ensuring that the nutritional goals are personalized and tailored to each user's specific health requirements."
    },
    {
      question: "How can I track my progress in Nutrigains?",
      answer: "The 'View Nutrition Intake' feature enables users to monitor and review their daily nutritional intake within the Nutrigains system. This feature provides valuable insights into dietary habits, allowing users to track their consumption of essential nutrients and make informed adjustments to their diet. The system presents this information in graphical bars, enhancing the visibility and tracking experience."
    },
    {
      question: "Is Nutrigains available as a mobile app?",
      answer: "No, Nutrigains is currently available exclusively as a web-based platform. While there is no mobile app available, users can still access all the features and functionalities of Nutrigains through their web browser on any device."
    },
    {
      question: "How can I sign up for Nutrigains?",
      answer: "Signing up for Nutrigains is easy! Simply visit our website and click on the 'Sign Up' button. Follow the on-screen instructions to create your account by providing the required information, and you'll be ready to start using Nutrigains right away, directly from your web browser."
    },
    {
      question: "How can I get support if I have questions or issues?",
      answer: "If you have any questions or encounter any issues while using Nutrigains, our customer support team is here to help. You can reach out to us through the contact form on our website or send us an email at support@nutrigains.com. We're committed to providing you with the assistance you need to make the most out of your Nutrigains experience."
    },
    {
      question: "Are there any subscription fees to use Nutrigains?",
      answer: "No, Nutrigains is currently available to users for free. There are no subscription fees or hidden charges associated with using the platform. Simply sign up for an account and start exploring the features and functionalities of Nutrigains at no cost."
    }
  ];
  

const FaqPage = () => {
  const [activeIndex, setActiveIndex] = useState(null);

  const handleToggle = (index) => {
    setActiveIndex(activeIndex === index ? null : index);
  };

  return (
    <>
      <Navbar />
      <div className="faq-container">
        <h1>FAQs</h1>
        {questionsAnswers.map((qa, index) => (
          <div key={index} className="faq-item">
            <button className="faq-question" onClick={() => handleToggle(index)}>
              {qa.question}
            </button>
            <div className={`faq-answer show`}>
              {qa.answer}
            </div>
          </div>
        ))}
      </div>
    </>
  );
};

export default FaqPage;
