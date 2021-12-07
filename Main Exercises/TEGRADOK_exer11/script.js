/*
Exercise 11 - Programming Languages, JavaScript - capturing HTML inputs and JavaScript events

CMSC 12 | Course

Submitted to:
Professor Aragones

Submitted by:
TEGRADO, Kenneth Renz A.
*/

// USE STRICT MODE
'use strict';

// Global variables
let diet; // dietary restrictions
let calories = 0; // calorie counter

// Variables for styling
let backgroundStyles = document.querySelector('body').style;
let formStyles = document.querySelector('form').style;
let titleStyles = document.querySelector('h2').style;
let buttonStyles = document.querySelector('.btn-grad').style;

// Functions
// Changing to vegetarianMode
const vegetarianMode = () => {
    // Change backgroundImage to Green
    backgroundStyles.backgroundImage =
        'radial-gradient( circle farthest-corner at 10% 20%,  rgba(14,174,87,1) 0%, rgba(12,116,117,1) 90% )';
    // Change form styles
    formStyles.background = '#ebf4ef';
    titleStyles.color = '#062e18';
    formStyles.boxShadow = '0 0 50px 2px #0b703a';
    // Change button styles
    buttonStyles.backgroundImage =
        'linear-gradient(to right, #348F50 0%, #56B4D3  51%, #348F50  100%)';
};

// Changing to noneMode
const noneMode = () => {
    // Change backgroundImage to Orange
    backgroundStyles.backgroundImage =
        'radial-gradient(circle farthest-corner at 10% 20%,rgba(255, 209, 67, 1) 0%,rgba(255, 145, 83, 1) 90% )';
    // Change form styles
    formStyles.background = '#fff6e5';
    titleStyles.color = '#4e423b';
    formStyles.boxShadow = '0 0 50px 10px #e87332';
    // Change button styles
    buttonStyles.backgroundImage =
        'linear-gradient(to right,#ff512f 0%,#f09819 51%,#ff512f 100%)';
};

// Changing to low carb dietary restriction
const lowCarbMode = () => {
    // Change backgroundImage to Orange
    backgroundStyles.backgroundImage =
        'radial-gradient( circle farthest-corner at 10% 20%,  rgba(171,102,255,1) 0%, rgba(116,182,247,1) 90% )';
    // Change form styles
    formStyles.background = '#f9f4ff';
    titleStyles.color = '#31194e';
    formStyles.boxShadow = '0 0 50px 1px #7f51b8';
    // Change button styles
    buttonStyles.backgroundImage =
        'linear-gradient(to right, #4776E6 0%, #8E54E9  51%, #4776E6  100%)';
};

document.getElementsByName('dietaryRestrictions').forEach((selection) => {
    selection.addEventListener('click', () => {
        diet = selection.value;
        if (diet === 'vegetarian') vegetarianMode();
        if (diet === 'noRestriction') noneMode();
        if (diet === 'lowCarb') lowCarbMode();
    });
});
