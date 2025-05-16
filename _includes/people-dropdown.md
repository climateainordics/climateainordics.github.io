<label for="tagFilter">Filter people:</label>
<select id="tagFilter">
<option value="all">Show All</option>
<option value="AI For Climate Education">AI For Climate Education (1)</option>
<option value="Atmospheric Science">Atmospheric Science (1)</option>
<option value="Bayesian Optimisation">Bayesian Optimisation (1)</option>
<option value="Biodiversity">Biodiversity (51)</option>
<option value="Climate Impacts">Climate Impacts (2)</option>
<option value="Climate Modeling">Climate Modeling (56)</option>
<option value="Climate Policy">Climate Policy (1)</option>
<option value="Computer Vision">Computer Vision (61)</option>
<option value="Deep Learning">Deep Learning (86)</option>
<option value="Earth Observation">Earth Observation (66)</option>
<option value="Ecosystem Monitoring and Modelling">Ecosystem Monitoring and Modelling (1)</option>
<option value="Ecosystem Services">Ecosystem Services (1)</option>
<option value="Education">Education (1)</option>
<option value="Efficient or Sustainable AI">Efficient or Sustainable AI (46)</option>
<option value="Environment Impacts of AI">Environment Impacts of AI (1)</option>
<option value="Extreme Weather">Extreme Weather (1)</option>
<option value="Fluid Dynamics">Fluid Dynamics (1)</option>
<option value="GIS">GIS (1)</option>
<option value="Geomatics">Geomatics (1)</option>
<option value="HPC">HPC (1)</option>
<option value="Impact on Climate Change on Health">Impact on Climate Change on Health (1)</option>
<option value="Knowledge Graphs">Knowledge Graphs (1)</option>
<option value="Machine Learning">Machine Learning (100)</option>
<option value="Machine Listening">Machine Listening (2)</option>
<option value="Marine Ecology">Marine Ecology (16)</option>
<option value="Materials">Materials (1)</option>
<option value="Meteorology">Meteorology (1)</option>
<option value="Molecular Modeling of Atmospheric Chemistry">Molecular Modeling of Atmospheric Chemistry (2)</option>
<option value="NLP">NLP (27)</option>
<option value="Numerical Weather Prediction">Numerical Weather Prediction (1)</option>
<option value="One Health">One Health (1)</option>
<option value="Public Health">Public Health (1)</option>
<option value="Remote Sensing">Remote Sensing (1)</option>
<option value="Soundscape Analysis">Soundscape Analysis (18)</option>
<option value="Spatial Analysis">Spatial Analysis (1)</option>
<option value="Species Distribution Modelling">Species Distribution Modelling (1)</option>
<option value="Stochastic Modelling and Distributions">Stochastic Modelling and Distributions (1)</option>
<option value="Sustainable Cities">Sustainable Cities (37)</option>
<option value="Sustainable Energy">Sustainable Energy (1)</option>
<option value="Sustainable Heating">Sustainable Heating (1)</option>
<option value="Sustainable Production">Sustainable Production (22)</option>
<option value="Sustainable Space Exploration and Research">Sustainable Space Exploration and Research (1)</option>
<option value="Sustainable Transport">Sustainable Transport (20)</option>
<option value="Urban Planning">Urban Planning (28)</option>
<option value="Use of Weather and Climate Data Outside of Academia">Use of Weather and Climate Data Outside of Academia (1)</option>
<option value="Visual Analytics">Visual Analytics (1)</option>
<option value="Visualization">Visualization (1)</option>
<option value="Weather Forecasting">Weather Forecasting (1)</option>
<option value="Wind Energy">Wind Energy (1)</option></select>

<script>
        document.getElementById('tagFilter').addEventListener('change', function () {
            const selectedTag = this.value;
            document.querySelectorAll('.content').forEach(div => {
                const tags = div.getAttribute('data-tags').split(',');
                if (selectedTag === 'all' || tags.includes(selectedTag)) {
                    div.classList.remove('hidden');
                } else {
                    div.classList.add('hidden');
                }
            });
        });
</script>

