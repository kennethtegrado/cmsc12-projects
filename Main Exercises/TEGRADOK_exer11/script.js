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
let selectionCount = 0; // selection count
let carbohydratesCount = 0; // number of carbohydrates meal
let vegetables = 0; //vegetables added

// button component and checkboxes
const button = document.querySelector('button'); // accessing the button component
const inputs = document.querySelectorAll('input[type="checkbox"]'); // variable for all the input instances of our checkboxes
const meatContainer = document.querySelector('#meatContainer'); // variable for all items that are meat
const firstFood = document.getElementById('firstFood'); // variable for accessing our first food checkbox for form validation
const form = document.querySelector('form'); // variable for accessing our form

// Variables for styling
let backgroundStyles = document.querySelector('body').style; // style for the background of the body
let formStyles = document.querySelector('form').style; // style for the form itself
let titleStyles = document.querySelector('h2').style; // style for the title Meal Planner
let buttonStyles = document.querySelector('.btn-grad').style; // style for the buttons

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

    // removing meat options
    meatContainer.classList.add('hidden');
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

    // Bringing back meat options if it was removed
    meatContainer.classList.remove('hidden');
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

    // Bringing meat options if it was removed
    meatContainer.classList.remove('hidden');
};

// Form Submission with Validation
form.addEventListener('submit', (event) => {
    // Iterate over all instances of the checkbox
    inputs.forEach((item) => {
        // Add one to our counter everytime that a checbox was clicked
        if (item.checked) {
            selectionCount++;
            // Add the values of the items checked to our calories
            calories += item.value;
            // Check the number of carbohydrates checked
            if (item.name === 'carbo') carbohydratesCount++;
            // Check the number of vegetables added
            else if (item.name === 'vegetables') vegetables++;
        }
    });

    // If the selection count is less than two then prevent form submission and display validation message
    if (selectionCount < 2) {
        // prevent form submission
        event.preventDefault();
        // validity message
        firstFood.setCustomValidity(
            'Please pick at least two food through the checkbox!'
        );
    } else {
        // Store calorie value
        if (diet === 'lowCarb') {
        }
    }
});

// Statement for updating our modes of planner
document.getElementsByName('dietaryRestrictions').forEach((selection) => {
    // for every instance of selection check if it was clicked
    selection.addEventListener('click', () => {
        // store the value of the selection to our diet
        diet = selection.value;
        // checked what selection is pressed by the user then set what mode is picked
        if (diet === 'vegetarian') vegetarianMode();
        if (diet === 'noRestriction') noneMode();
        if (diet === 'lowCarb') lowCarbMode();
    });
});
