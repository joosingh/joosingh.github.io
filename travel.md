---
layout: default
title: Travel
---

# Travel

<style>
.travel-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 1rem;
  justify-content: center;
  margin-top: 1.5rem;
}

.country-card {
  width: 220px;
  height: 140px;
  border-radius: 8px;
  background-size: cover;
  background-position: center;
  position: relative;
  cursor: pointer;
  box-shadow: 0 4px 8px rgba(0,0,0,0.2);
  transition: transform 0.3s ease;
}
.country-card:hover {
  transform: scale(1.05);
}

.country-name {
  position: absolute;
  bottom: 0;
  width: 100%;
  background: rgba(0,0,0,0.6);
  color: #fff;
  text-align: center;
  padding: 0.4rem;
  border-bottom-left-radius: 8px;
  border-bottom-right-radius: 8px;
  font-weight: bold;
}

/* Photo section */
.country-photos {
  display: none;
  flex-wrap: wrap;
  justify-content: center;
  gap: 1rem;
  margin: 2rem 0;
}

.country-photos.active {
  display: flex;
}

.photo-card {
  width: 260px;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  transition: transform 0.3s ease;
}
.photo-card img {
  width: 100%;
  display: block;
}
.photo-card:hover {
  transform: scale(1.03);
}
</style>

<div class="travel-grid">
  <div class="country-card" style="background-image: url('/assets/travels/USA/nyc1.jpeg');" onclick="showPhotos('USA')">
    <div class="country-name">USA</div>
  </div>
  <div class="country-card" style="background-image: url('/assets/travels/thailand/bangkok.jpg');" onclick="showPhotos('thailand')">
    <div class="country-name">Thailand</div>
  </div>
  <div class="country-card" style="background-image: url('/assets/travels/germany/berlin.jpg');" onclick="showPhotos('germany')">
    <div class="country-name">Germany</div>
  </div>
  <div class="country-card" style="background-image: url('/assets/travels/singapore/marina_bay.jpg');" onclick="showPhotos('singapore')">
    <div class="country-name">Singapore</div>
  </div>
</div>

<!-- Country Photo Sections -->

<div id="usa" class="country-photos">
  <div class="photo-card"><img src="/assets/travels/USA/nyc1.jpeg" alt="New York1"></div>
  <div class="photo-card"><img src="/assets/travels/USA/nyc2.jpeg" alt="New York2"></div>
</div>

<div id="thailand" class="country-photos">
  <div class="photo-card"><img src="/assets/travels/thailand/bangkok.jpg" alt="Bangkok"></div>
  <div class="photo-card"><img src="/assets/travels/thailand/phuket.jpg" alt="Phuket"></div>
</div>

<div id="germany" class="country-photos">
  <div class="photo-card"><img src="/assets/travels/germany/berlin.jpg" alt="Berlin"></div>
</div>

<div id="singapore" class="country-photos">
  <div class="photo-card"><img src="/assets/travels/singapore/marina_bay.jpg" alt="Marina Bay"></div>
</div>

<script>
function showPhotos(countryId) {
  // Hide all
  document.querySelectorAll('.country-photos').forEach(div => {
    div.classList.remove('active');
  });

  // Show selected
  const selected = document.getElementById(countryId);
  if (selected) {
    selected.classList.add('active');
    // Scroll to photos
    selected.scrollIntoView({ behavior: 'smooth' });
  }
}
</script>
