<label for="tagFilter">Filter people:</label>
<select id="tagFilter">
<option value="all">Show All</option>
<option value="Bayesian Optimisation">Bayesian Optimisation (1)</option>
<option value="Biodiversity">Biodiversity (35)</option>
<option value="Climate Impacts">Climate Impacts (1)</option>
<option value="Climate Modeling">Climate Modeling (32)</option>
<option value="Climate Policy">Climate Policy (1)</option>
<option value="Computer Vision">Computer Vision (42)</option>
<option value="Deep Learning">Deep Learning (57)</option>
<option value="Earth Observation">Earth Observation (44)</option>
<option value="Ecosystem Monitoring and Modelling">Ecosystem Monitoring and Modelling (1)</option>
<option value="Ecosystem Services">Ecosystem Services (1)</option>
<option value="Education">Education (1)</option>
<option value="Efficient or Sustainable AI">Efficient or Sustainable AI (29)</option>
<option value="Environment Impacts of AI">Environment Impacts of AI (1)</option>
<option value="Extreme Weather">Extreme Weather (1)</option>
<option value="Fluid Dynamics">Fluid Dynamics (1)</option>
<option value="GIS">GIS (1)</option>
<option value="Geomatics">Geomatics (1)</option>
<option value="HPC">HPC (1)</option>
<option value="Impact On Climate Change On Health">Impact On Climate Change On Health (1)</option>
<option value="Knowledge Graphs">Knowledge Graphs (1)</option>
<option value="Machine Learning">Machine Learning (60)</option>
<option value="Machine Listening">Machine Listening (2)</option>
<option value="Marine Ecology">Marine Ecology (11)</option>
<option value="Materials and Atmospheric Science">Materials and Atmospheric Science (1)</option>
<option value="Meteorology">Meteorology (1)</option>
<option value="Molecular Modeling of Atmospheric Chemistry">Molecular Modeling of Atmospheric Chemistry (1)</option>
<option value="NLP">NLP (16)</option>
<option value="Remote Sensing">Remote Sensing (1)</option>
<option value="Soundscape Analysis">Soundscape Analysis (14)</option>
<option value="Spatial Analysis">Spatial Analysis (1)</option>
<option value="Sustainable Cities">Sustainable Cities (21)</option>
<option value="Sustainable Production">Sustainable Production (15)</option>
<option value="Sustainable Space Exploration and Research">Sustainable Space Exploration and Research (1)</option>
<option value="Sustainable Transport">Sustainable Transport (12)</option>
<option value="Urban Planning">Urban Planning (13)</option>
<option value="Weather Forecasting">Weather Forecasting (1)</option></select>

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

