# flypad-plots
scripts for plotting flyPAD capacitance data and metadata using niceplot

# TH fragments flyPAD dataset
###### ID: #DG-FP-0001
###### LINK: []
###### Experimentor: Célia
***
## Abstract:
This is dataset in order to test the TH fragments from Mark Wu's Lab (for reference see Liu et al., 2017) using the flyPAD setup in the behavior room. Célia did the experiments on ... ...

The experiment has two parts:
1. Célia did initial tests on lines that have been ordered earlier. These experiments (group A) were performed from 24th to 26th May.
2. Later, Célia carried experiments on lines that have been requested in response to the publication of Liu et al. (2017). These experiments (group B) were performed from 4th August.

## Workflow:
- [ ] cleaned metadata
- [ ] plotting
- [ ] interpretation

## Glossary:
* FF = fully fed:
* 3dd = 3 days deprived:
* V = virgin
* M = mated
* f = female
* m = male

## Conditions:
For the experiments, we use different geneotypes (e.g., *R70G12-GAL4*), metabolic state (e.g., *FF*), sex (e.g., *f*), mating state (e.g., *V*) and assay temperature (e.g., *22*) in ºC. Dates are given in the format *DD-MM-YY*.

### Group A:

|    Date | Condition No. | GAL4 driver | UAS effector | Metabolic state | Mating state | Sex | Temperature (ºC) |
|    ---- | ------------- | ----------- | ------------ | --------------- | ------------ | --- | ---------------- |
| 24-05-17|            01 | R70G12-GAL4 |    UAS-dTrpA1|               FF|             ?|    f|                22|
| 24-05-17|            02 | R72B03-GAL4 |    UAS-dTrpA1|               FF|             ?|    f|                22|
| 24-05-17|            03 | empty-GAL4  |    UAS-dTrpA1|               FF|             ?|    f|                22|
| 24-05-17|            04 | R70G12-GAL4 |    UAS-dTrpA1|              3dd|             ?|    f|                22|
| 24-05-17|            05 | R72B03-GAL4 |    UAS-dTrpA1|              3dd|             ?|    f|                22|
| 24-05-17|            06 | empty-GAL4  |    UAS-dTrpA1|              3dd|             ?|    f|                22|
| 24-05-17|            07 | R70G12-GAL4 |    UAS-dTrpA1|               FF|             ?|    f|                30|
| 24-05-17|            08 | R72B03-GAL4 |    UAS-dTrpA1|               FF|             ?|    f|                30|
| 24-05-17|            09 | empty-GAL4  |    UAS-dTrpA1|               FF|             ?|    f|                30|
| 24-05-17|            10 | R70G12-GAL4 |    UAS-dTrpA1|              3dd|             ?|    f|                30|
| 24-05-17|            11 | R72B03-GAL4 |    UAS-dTrpA1|              3dd|             ?|    f|                30|
| 24-05-17|            12 | empty-GAL4  |    UAS-dTrpA1|              3dd|             ?|    f|                30|
| 25-05-17|            01 | TH-C4-GAL4  |    UAS-dTrpA1|               FF|             V|    f|                22|
| 25-05-17|            02 | TH-C'-GAL4  |    UAS-dTrpA1|               FF|             V|    f|                22|
| 25-05-17|            03 | TH-D1-GAL4  |    UAS-dTrpA1|               FF|             V|    f|                22|
| 25-05-17|            04 | TH-D4-GAL4  |    UAS-dTrpA1|               FF|             V|    f|                22|
| 25-05-17|            05 | TH-D'-GAL4  |    UAS-dTrpA1|               FF|             V|    f|                22|
| 25-05-17|            06 | empty-GAL4  |    UAS-dTrpA1|               FF|             V|    f|                22|
| 25-05-17|            07 | R70G12-GAL4 |    UAS-dTrpA1|               FF|             V|    f|                30|    <!-- not sure, ask Célia -->
| 25-05-17|            08 | R72B03-GAL4 |    UAS-dTrpA1|               FF|             V|    f|                30|    <!-- not sure, ask Célia -->
| 25-05-17|            09 | empty-GAL4  |    UAS-dTrpA1|               FF|             V|    f|                30|    <!-- not sure, ask Célia -->
| 25-05-17|            10 | R70G12-GAL4 |    UAS-dTrpA1|              3dd|             V|    f|                30|    <!-- not sure, ask Célia -->
| 25-05-17|            11 | R72B03-GAL4 |    UAS-dTrpA1|              3dd|             V|    f|                30|    <!-- not sure, ask Célia -->
| 25-05-17|            12 | empty-GAL4  |    UAS-dTrpA1|              3dd|             V|    f|                30|    <!-- not sure, ask Célia -->
| 26-05-17|            01 | TH-C4-GAL4  |    UAS-dTrpA1|               FF|             V|    f|                22|
| 26-05-17|            02 | TH-C'-GAL4  |    UAS-dTrpA1|               FF|             V|    f|                22|
| 26-05-17|            03 | TH-D1-GAL4  |    UAS-dTrpA1|               FF|             V|    f|                22|
| 26-05-17|            04 | TH-D4-GAL4  |    UAS-dTrpA1|               FF|             V|    f|                22|
| 26-05-17|            05 | TH-D'-GAL4  |    UAS-dTrpA1|               FF|             V|    f|                22|
| 26-05-17|            06 | empty-GAL4  |    UAS-dTrpA1|               FF|             V|    f|                22|
| 26-05-17|            07 | R70G12-GAL4 |    UAS-dTrpA1|               FF|             V|    f|                30|    <!-- not sure, ask Célia -->
| 26-05-17|            08 | R72B03-GAL4 |    UAS-dTrpA1|               FF|             V|    f|                30|    <!-- not sure, ask Célia -->
| 26-05-17|            09 | empty-GAL4  |    UAS-dTrpA1|               FF|             V|    f|                30|    <!-- not sure, ask Célia -->
| 26-05-17|            10 | R70G12-GAL4 |    UAS-dTrpA1|              3dd|             V|    f|                30|    <!-- not sure, ask Célia -->
| 26-05-17|            11 | R72B03-GAL4 |    UAS-dTrpA1|              3dd|             V|    f|                30|    <!-- not sure, ask Célia -->
| 26-05-17|            12 | empty-GAL4  |    UAS-dTrpA1|              3dd|             V|    f|                30|    <!-- not sure, ask Célia -->

### Group B:



## Substrates:
* channel 1: 10% yeast
* channel 2: 20 mM sucrose

## File structure:

## Sessions metadata:
The sessions metadata (mapping files-metadata)

## Results:

## Discussion:

## References:
* Liu Q, Tabuchi M, Liu S, Kodama L, Horiuchi W, Daniels J, Chiu L, Baldoni D, Wu MN. Branch-specific plasticity of a bifunctional dopamine circuit encodes protein hunger. Science. 2017 May 5;356(6337):534-9.
