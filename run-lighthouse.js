const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const mainPages = [
  'index.html',
  'Aboutus.html',
  'Contactus.html',
  'whatwedo.html',
  'Portfolio.html',
  'Case-Studies.html',
  'Client-Testimonials.html',
  'Insights.html',
  'Projects-Handled.html',
  'Success-Stories.html',
  'Transformations.html',
  'FAQ-India.html',
  'FAQ-MiddleEast.html',
  'Pathik-Grand.html',
  'ArdenaHotels.html',
  'Hospitality-Audit.html',
  'Hospitality-Commercial.html',
  'Hospitality-Consulting.html',
  'Hospitality-Training.html',
  'Hotel-Management.html',
  'Hotel-Pre-Opening.html',
  'Hotel-Revenue-Management.html',
  'Resort-Management.html',
  'Book-Audit.html',
  'Book-Consultation.html',
  'Download-Brochure.html',
  'Join-Newsletter.html',
  'Request-Proposal.html',
];

const outputDir = './lighthouse-results';
if (!fs.existsSync(outputDir)) {
  fs.mkdirSync(outputDir, { recursive: true });
}

const baseUrl = 'http://localhost:8080';

for (const page of mainPages) {
  const url = `${baseUrl}/${page}`;
  const outputFile = path.join(outputDir, `lighthouse-${page.replace('.html', '')}.json`);
  
  console.log(`Running Lighthouse on ${url}...`);
  
  try {
    execSync(`npx lighthouse "${url}" --output=json --output-path="${outputFile}" --chrome-flags="--headless --no-sandbox --disable-gpu" --quiet`, {
      stdio: 'inherit',
      timeout: 120000
    });
    console.log(`✓ Saved to ${outputFile}`);
  } catch (error) {
    console.error(`✗ Failed for ${page}:`, error.message);
  }
}

console.log('All Lighthouse audits completed!');