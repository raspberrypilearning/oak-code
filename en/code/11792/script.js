// Show/Hide Eco Tips
document.getElementById('toggleTipsBtn').addEventListener('click', () => {
  const tips = document.getElementById('ecoTips');
  tips.classList.toggle('hidden');
});

// Accordion Buttons
const accordionButtons = document.querySelectorAll('.accordionBtn');
accordionButtons.forEach(button => {
  button.addEventListener('click', () => {
    const targetId = button.getAttribute('data-target');
    document.getElementById(targetId).classList.toggle('hidden');
  });
});

// Eco Tip Alert Button
document.getElementById('ecoTipBtn').addEventListener('click', () => {
  alert('Tip: Bring a reusable coffee cup to avoid single-use cups.');
});

// Quiz Answer Buttons
const quizButtons = document.querySelectorAll('.quizBtn');
quizButtons.forEach(button => {
  button.addEventListener('click', () => {
    const answer = button.getAttribute('data-answer');
    const result = document.getElementById('quizResult');
    if (answer === 'B') {
      result.innerText = 'Correct! Reusable bottles reduce plastic waste.';
      result.style.color = 'green';
    } else {
      result.innerText = 'Incorrect. Try again!';
      result.style.color = 'red';
    }
  });
});

// Hover Effect on Eco Fact
const ecoFact = document.getElementById('ecoFact');
ecoFact.addEventListener('mouseover', () => {
  ecoFact.style.backgroundColor = '#FFEB3B';
});
ecoFact.addEventListener('mouseout', () => {
  ecoFact.style.backgroundColor = 'transparent';
});
