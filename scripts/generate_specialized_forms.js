function createSpecializedForms() {

    // --- FORM 1: PRODUCTION SERVICES (Video/Edit/Write) ---
    var formProd = FormApp.create('Chaues Productions - Production Services');
    formProd.setDescription('Videography, Editing, Writing, and Creative Direction inquiries.');
    formProd.setCollectEmail(true);

    formProd.addTextItem().setTitle('Name').setRequired(true);
    formProd.addMultipleChoiceItem()
        .setTitle('Service Needed')
        .setChoiceValues(['Videography (Filming)', 'Editing/Post-Production', 'Writing/Copyediting', 'Directing/Creative Lead', 'Full Production'])
        .setRequired(true);

    formProd.addMultipleChoiceItem()
        .setTitle('Project Location')
        .setChoiceValues(['Nashville, TN (Local)', 'Remote', 'Travel Required (Expenses Covered)'])
        .setRequired(true);

    formProd.addParagraphTextItem()
        .setTitle('Project Description')
        .setHelpText('Please describe your vision, timeline, and deliverables.')
        .setRequired(true);

    formProd.addMultipleChoiceItem()
        .setTitle('Budget Range')
        .setChoiceValues(['Under $1k', '$1k - $3k', '$3k - $5k', '$5k+', 'TBD'])
        .setRequired(true);

    // --- FORM 2: TRIP PLANNING & GUIDE SERVICES ---
    var formPlan = FormApp.create('Chaues - Trip Planning & Guide Services');
    formPlan.setDescription('Custom Japan itineraries, virtual planning sessions, and on-site guide services.');
    formPlan.setCollectEmail(true);

    formPlan.addTextItem().setTitle('Name').setRequired(true);

    formPlan.addCheckboxItem()
        .setTitle('Services Interested In')
        .setChoiceValues([
            'Virtual Planning Session (Consultation)',
            'Custom Itinerary Creation (I map it, you travel)',
            'On-Site Guide (I travel with you/meet you)',
            'Logistical Support'
        ])
        .setRequired(true);

    formPlan.addTextItem().setTitle('Proposed Dates').setHelpText('When are you planning to go?').setRequired(true);
    formPlan.addTextItem().setTitle('Group Size').setRequired(true);

    formPlan.addParagraphTextItem()
        .setTitle('Trip Goals / Interests')
        .setHelpText('What do you want to experience? (e.g. History, hidden gems, anime locations, food, hiking)');

    formPlan.addParagraphTextItem()
        .setTitle('Any specific request?');

    // --- FORM 3: TOKYO / JAPAN PARTNERSHIPS ---
    var formTokyo = FormApp.create('Tokyo in Film - Partnerships & Inquiries');
    formTokyo.setDescription('For companies in Japan, course partnerships, and specific Tokyo availability.');
    formTokyo.setCollectEmail(true);

    formTokyo.addTextItem().setTitle('Organization / Company Name').setRequired(true);
    formTokyo.addTextItem().setTitle('Contact Person').setRequired(true);

    formTokyo.addMultipleChoiceItem()
        .setTitle('Inquiry Type')
        .setChoiceValues([
            'Partnership with "Tokyo in Film" Course',
            'Hiring for May 2026 (Tokyo On-Site)',
            'Sponsorship',
            'General Japan Business Inquiry'
        ])
        .setRequired(true);

    formTokyo.addParagraphTextItem()
        .setTitle('Message / Proposal')
        .setHelpText('How would you like to collaborate?')
        .setRequired(true);

    // --- LOG URLs ---
    Logger.log('--- FORMS CREATED ---');
    Logger.log('Production URL: ' + formProd.getPublishedUrl());
    Logger.log('Planning URL: ' + formPlan.getPublishedUrl());
    Logger.log('Tokyo URL: ' + formTokyo.getPublishedUrl());
}
