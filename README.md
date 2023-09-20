# dengue

## Description of the Datasets
We took primary human dendritic cells, infected them with dengue virus (serotype 3) and subjected these cells to either:

siRNA screening to identify human host factors that act to restrict viral replication,
Proteomics (Protein Abundance) to look at human proteins that change in abundance following infection.
This was done at 24h and 48h post infection. (Jeff Johnson, Krogan lab)
RNAseq to look at cellular mRNAs that are differently expressed following infection.
This was done at 24h and 48h post infection. (Stephen Wolinski, NWU)
We also include host-dengue PPI data from (Shah et al., Cell 2018). Priya Shah was at the Krogan lab when this data was collected

The datasets are already thresholded based maximum overlap and significance, and all have GeneID as common identifier.

20220202_Thresholded_Datasets_DHIPC.xlsx

Shah et al., Dengue Interactions


## Purpose of the Analysis

1. Identify proteins meeting the following criteria

 - negatively affect dengue virus replication when inhibited by siRNA*
 AND
 - are either:
        - modulated in protein abundance
        - modulated in rna abundance
        - interact with the dengue virus
        
2. Identify systems of interacting proteins enriched in those that affect dengue replication

* \*the highest the Zscore, the more these factors negatively affect dengue virus replication

3. Characterize the systems:
 - Name them by top hits from gProfiler enrichment
 - Name them using GPT-4
 - Analyze the systems with GPT-4
     - General analysis
     - Specific analyses in which data associated with the proteins is provided. This will be a matter of experimentation. Probably most tractable for small systems. We can try specifically asking for interpretation of the system for its role in response to dengue infection.

4. Other points:
 - How should we interpret the 24 vs 48 hour data?
 - What visualization strategies will work best?


## Data Loading
 - Used ChatGPT data analyis to merge the sheets in the original excel file provided by Laura
     - Added a boolean column "binds_viral_protein" based on the viral interaction data
     - Added boolean columns indicating whether the protein had significant values for the various measurements

## Hierarchical Model Building
 - Made an network of interactions between the proteins: STRING HC
     - Next step - add dengue AP-MS
 - Made a hierarchical from the subnetwork interconnecting the proteins of interest
 - Named the model systems by enrichment
 
## TODO
 - Name and some or all of the model systems by LLM
 - Identify goal proteins
 - Identify systems enriched with goal proteins
 - Style the model and the interactome to highlight the data
 - Generate reports
 - Generate figures
 




