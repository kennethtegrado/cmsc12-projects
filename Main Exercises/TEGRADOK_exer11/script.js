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
    formStyles.boxShadow = '0 0 100px 10px #264635';
    // Change button styles
    buttonStyles.backgroundImage =
        'linear-gradient(to right, #348F50 0%, #56B4D3  51%, #348F50  100%)';
};

// Changing to noneMode
const noneMode = () => {
    // Change backgroundImage to Orange
    backgroundStyles.backgroundImage =
        'linear-gradient(to right, #ff512f 0%, #f09819 51%, #ff512f 100%)';
    // Change form styles
    formStyles.background = '#fff6e5';
    titleStyles.color = '#9f5913';
    formStyles.boxShadow = '0 0 50px 10px #e87332';
    // Change button styles
    buttonStyles.backgroundImage =
        'linear-gradient(to right,#ff512f 0%,#f09819 51%,#ff512f 100%)';
};

document.getElementsByName('dietaryRestrictions').forEach((selection) => {
    selection.addEventListener('click', () => {
        const choice = selection.value;
        if (choice === 'vegetarian') vegetarianMode();

        if (choice === 'noRestriction') noneMode();
    });
});
