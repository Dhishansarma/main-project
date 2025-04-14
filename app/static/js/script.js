// Load Header


// Load Footer
fetch('footer.html')
    .then(response => response.text())
    .then(data => document.getElementById('footer').innerHTML = data);

    document.getElementById("workshopBookingForm").addEventListener("submit", function(event) {
        event.preventDefault();
        document.getElementById("confirmationMessage").style.display = "block";
    });
    
    /*Workshop Submit*/
document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("workshopBookingForm");
    const confirmationMessage = document.getElementById("confirmationMessage");

    form.addEventListener("submit", function (event) {
        event.preventDefault(); // Prevent form submission
        
        confirmationMessage.style.display = "block"; // Show confirmation message

        setTimeout(() => {
            location.reload(); // Refresh the page after 5 seconds
        }, 5000);
    });
});

/*Careers Submit */
document.getElementById("careerForm").addEventListener("submit", function(event) {
    event.preventDefault();
    
    document.getElementById("submitBtn").innerText = "Submitted";
    document.getElementById("submitBtn").disabled = true;
    document.getElementById("confirmationMessage").style.display = "block"; // Show message

    // Refresh the page after 3 seconds
    setTimeout(() => {
        location.reload();
    }, 3000);
});

// Add this inside your <body> tag at the bottom OR in script.js
document.querySelectorAll('.dd-trigger').forEach(trigger => {
    trigger.addEventListener('click', function(e) {
        e.preventDefault();
        const parentLi = this.parentElement;
        parentLi.classList.toggle('active-dropdown');
    });
});

const productsBtn = document.getElementById('productsBtn');
    const productsDropdown = document.getElementById('productsDropdown');

    const servicesBtn = document.getElementById('servicesBtn');
    const servicesDropdown = document.getElementById('servicesDropdown');

    // Toggle dropdown on click
    productsBtn.addEventListener('click', function(e) {
      e.stopPropagation();
      productsDropdown.classList.toggle('show');
      servicesDropdown.classList.remove('show');
    });

    servicesBtn.addEventListener('click', function(e) {
      e.stopPropagation();
      servicesDropdown.classList.toggle('show');
      productsDropdown.classList.remove('show');
    });

    // Close dropdown when clicking outside
    window.addEventListener('click', function() {
      productsDropdown.classList.remove('show');
      servicesDropdown.classList.remove('show');
    });

   