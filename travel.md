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

.country-photos {
  display: none;
  flex-wrap: wrap;
  justify-content: center;
  gap: 1rem;
  margin: 2rem 0;
}

.country-photos.active {
  display: flex;
  flex-wrap: wrap;
}

.photo-card {
  width: 260px;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
  cursor: pointer;
  transition: transform 0.3s ease;
}
.photo-card img {
  width: 100%;
  display: block;
}
.photo-card:hover {
  transform: scale(1.03);
}
.caption {
  font-size: 0.85rem;
  text-align: center;
  color: #666;
  margin-top: 0.5rem;
}

/* Lightbox */
#lightbox-modal {
  display: none;
  position: fixed;
  z-index: 9999;
  top: 0; left: 0;
  width: 100vw;
  height: 100vh;
  background: rgba(0,0,0,0.85);
  justify-content: center;
  align-items: center;
}
#lightbox-modal img {
  max-width: 90vw;
  max-height: 90vh;
  border-radius: 8px;
}
#lightbox-modal .close-btn {
  position: absolute;
  top: 20px;
  right: 30px;
  font-size: 2rem;
  color: white;
  cursor: pointer;
}
</style>

<!-- Grid of Countries -->
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

<!-- Country Photos -->
<div id="USA" class="country-photos">
  <div class="photo-card" onclick="openLightbox('/assets/travels/USA/nyc1.jpeg')">
    <img src="/assets/travels/USA/nyc1.jpeg" alt="NYC1">
    <div class="caption">caption1</div>
  </div>
  <div class="photo-card" onclick="openLightbox('/assets/travels/USA/nyc2.jpeg')">
    <img src="/assets/travels/USA/nyc2.jpeg" alt="NYC2">
    <div class="caption">caption2</div>
  </div>
</div>

<div id="thailand" class="country-photos">
  <div class="photo-card" onclick="openLightbox('/assets/travels/thailand/bangkok.jpg')">
    <img src="/assets/travels/thailand/bangkok.jpg" alt="Bangkok">
    <div class="caption">Bangkok’s street food is unmatched.</div>
  </div>
  <div class="photo-card" onclick="openLightbox('/assets/travels/thailand/phuket.jpg')">
    <img src="/assets/travels/thailand/phuket.jpg" alt="Phuket">
    <div class="caption">Sunset over Patong Beach 🌅</div>
  </div>
</div>

<div id="germany" class="country-photos">
  <div class="photo-card" onclick="openLightbox('/assets/travels/germany/berlin.jpg')">
    <img src="/assets/travels/germany/berlin.jpg" alt="Berlin">
    <div class="caption">Brandenburg Gate in Berlin 🇩🇪</div>
  </div>
</div>

<div id="singapore" class="country-photos">
  <div class="photo-card" onclick="openLightbox('/assets/travels/singapore/marina_bay.jpg')">
    <img src="/assets/travels/singapore/marina_bay.jpg" alt="Marina Bay">
    <div class="caption">Marina Bay Sands — futuristic skyline!</div>
  </div>
</div>

<!-- Lightbox Modal -->
<div id="lightbox-modal" onclick="closeLightbox()">
  <span class="close-btn" onclick="closeLightbox()">×</span>
  <img id="lightbox-img" src="" alt="Lightbox">
</div>

<script>
function showPhotos(countryId) {
  document.querySelectorAll('.country-photos').forEach(div => div.classList.remove('active'));
  document.getElementById(countryId).classList.add('active');
  document.getElementById(countryId).scrollIntoView({ behavior: 'smooth' });
}

function openLightbox(src) {
  document.getElementById('lightbox-img').src = src;
  document.getElementById('lightbox-modal').style.display = 'flex';
}

function closeLightbox() {
  document.getElementById('lightbox-modal').style.display = 'none';
}
</script>
