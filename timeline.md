---
layout: page
title: Timeline
---

<!-- Load timeline CSS inline -->
<style>
  .timeline {
    position: relative;
    max-width: 900px;
    margin: auto;
    padding: 1rem 0;
  }

  .timeline::after {
    content: '';
    position: absolute;
    width: 4px;
    background-color: #007acc;
    top: 0;
    bottom: 0;
    left: 50%;
    transform: translateX(-50%);
  }

  .timeline-entry {
    position: relative;
    width: 42%;
    padding: 1rem;
  }

  .timeline-entry.left {
    left: 0;
    margin-left: 4%;
    text-align: right;
  }

  .timeline-entry.right {
    left: 50%;
    text-align: left;
  }

  .timeline-entry::after {
    content: '';
    position: absolute;
    width: 18px;
    height: 18px;
    background-color: #fff;
    border: 4px solid #007acc;
    top: 1rem;
    border-radius: 50%;
    z-index: 1;
  }

  .timeline-entry.left::after {
    right: -10px;
  }

  .timeline-entry.right::after {
    left: -10px;
  }

  .content {
    background-color: white;
    padding: 1rem;
    border-radius: 6px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
  }

  .date {
    font-size: 0.9rem;
    color: #999;
    margin-bottom: 0.5rem;
  }

  @media screen and (max-width: 768px) {
    .timeline::after {
      left: 20px;
    }

    .timeline-entry {
      width: 100%;
      padding-left: 60px;
      padding-right: 25px;
      margin-left: 0;
      text-align: left;
    }

    .timeline-entry.left,
    .timeline-entry.right {
      left: 0;
    }

    .timeline-entry::after {
      left: 18px;
    }
  }
</style>


<div class="timeline">

  <div class="timeline-entry left">
    <div class="content">
      <div class="date">2013 – 2018</div>
      <h3>Undergraduate and Postgraduate - IIT (BHU) Varanasi</h3>
      <p>Pharmacy</p>
    </div>
  </div>

  <div class="timeline-entry right">
    <div class="content">
      <div class="date">2018 – 2022</div>
      <h3>Doctor of Philosphy - NTU Singapore</h3>
      <p>Biomaterials</p>
    </div>
  </div>

  <div class="timeline-entry left">
    <div class="content">
      <div class="date">Since Nov 2022</div>
      <h3>Postdoctoral Research Associate - Carnegie Mellon University, USA</h3>
      <p>Working on Biomaterials design using polymer chemistry</p>
    </div>
  </div>

  
</div>
