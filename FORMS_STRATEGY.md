# Form Strategy Guide: The 3-Form System

We have moved from a single complex form to **three specialized forms**. This structure is clearer for users and gives you better organization for incoming leads.

## 1. The Three Forms

### A. **Video & Production Services**
**Target Audience:** Clients who need videography, editing, writing, or creative direction.
**Key Questions:**
- Service Needed (Filming, Editing, Writing, etc.)
- Location (Nashville vs. Remote vs. Travel)
- Project Description & Budget

### B. **Trip Planning & Guide Services**
**Target Audience:** Travelers wanting Japan itineraries, virtual consultation, or an on-site guide.
**Key Questions:**
- Service: Virtual Planning vs. Custom Itinerary vs. On-Site Guide
- Travel Dates & Group Size
- Interests (History, Anime locations, Food, Hiking)

### C. **Tokyo & Partnerships**
**Target Audience:** Japanese companies, schools, or sponsors wanting to partner with "Tokyo in Film".
**Key Questions:**
- Inquiry Type: Course Partnership, May 2026 Hiring, Sponsorship
- Organization Name & Contact Person
- Partnership Proposal

---

## 2. Implementation Instructions

### Step 1: Generate the Forms
1. Open [Google Apps Script](https://script.google.com).
2. Create a **New Project**.
3. Copy the code from `scripts/generate_specialized_forms.js`.
4. Paste it into the editor and click **Run**.
5. **Grant Permission** when prompted.
6. The script will print **3 URLs** in the Execution Log at the bottom.

### Step 2: Update the Website
1. Copy the 3 URLs generated in Step 1.
2. Open `landing.html`.
3. Locate the `contact-grid` section (around line 500).
4. Replace the `href="#"` for each button with your new real Form URLs.

```html
<!-- Example -->
<a href="PUT_PRODUCTION_FORM_URL_HERE" class="contact-card">
    <strong>Video & Production</strong>
    ...
</a>
```

### Step 3: Test
- Click each button on your specific landing page to ensure it opens the correct specialized form.
