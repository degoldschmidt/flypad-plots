# flypad-plots
scripts for plotting flyPAD capacitance data and metadata using niceplot

# TH fragments flyPAD dataset
###### ID: #DG-FP-0001
###### LINK: []
###### Experimentor: Célia
***
## Abstract:
This is dataset in order to test the TH fragments from Mark Wu's Lab (for reference see Liu et al., 2017) using the flyPAD setup in the behavior room.

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

|      Date | Condition No. | GAL4 driver | UAS effector | Metabolic state | Mating state | Sex | Temperature (ºC) |
|      ---- | ------------- | ----------- | ------------ | --------------- | ------------ | --- | ---------------- |
|   24-05-17|            01 | R70G12-GAL4 |    UAS-dTrpA1|               FF|             ?|   f |            22    |
|   24-05-17|            02 | R72B03-GAL4 |    UAS-dTrpA1|               FF|             ?|   f |            22    |
|   24-05-17|            03 | empty-GAL4  |    UAS-dTrpA1|               FF|             ?|   f |            22    |
|   24-05-17|            04 | R70G12-GAL4 |    UAS-dTrpA1|              3dd|             ?|   f |            22    |
|   24-05-17|            05 | R72B03-GAL4 |    UAS-dTrpA1|              3dd|             ?|   f |            22    |
|   24-05-17|            06 | empty-GAL4  |    UAS-dTrpA1|              3dd|             ?|   f |            22    |
|   24-05-17|            07 | R70G12-GAL4 |    UAS-dTrpA1|               FF|             ?|   f |              30  |
|   24-05-17|            08 | R72B03-GAL4 |    UAS-dTrpA1|               FF|             ?|   f |              30  |
|   24-05-17|            09 | empty-GAL4  |    UAS-dTrpA1|               FF|             ?|   f |              30  |
|   24-05-17|            10 | R70G12-GAL4 |    UAS-dTrpA1|              3dd|             ?|   f |              30  |
|   24-05-17|            11 | R72B03-GAL4 |    UAS-dTrpA1|              3dd|             ?|   f |              30  |
|   24-05-17|            12 | empty-GAL4  |    UAS-dTrpA1|              3dd|             ?|   f |              30  |
|  25-05-17 |            01 | TH-C4-GAL4  |    UAS-dTrpA1|               FF|            V |   f |            22    |
|  25-05-17 |            02 | TH-C'-GAL4  |    UAS-dTrpA1|               FF|            V |   f |            22    |
|  25-05-17 |            03 | TH-D1-GAL4  |    UAS-dTrpA1|               FF|            V |   f |            22    |
|  25-05-17 |            04 | TH-D4-GAL4  |    UAS-dTrpA1|               FF|            V |   f |            22    |
|  25-05-17 |            05 | TH-D'-GAL4  |    UAS-dTrpA1|               FF|            V |   f |            22    |
|  25-05-17 |            06 | empty-GAL4  |    UAS-dTrpA1|               FF|            V |   f |            22    |
|  25-05-17 |            07 | R70G12-GAL4 |    UAS-dTrpA1|               FF|            V |   f |              30  |    <!-- not sure, ask Célia -->
|  25-05-17 |            08 | R72B03-GAL4 |    UAS-dTrpA1|               FF|            V |   f |              30  |    <!-- not sure, ask Célia -->
|  25-05-17 |            09 | empty-GAL4  |    UAS-dTrpA1|               FF|            V |   f |              30  |    <!-- not sure, ask Célia -->
|  25-05-17 |            10 | R70G12-GAL4 |    UAS-dTrpA1|              3dd|            V |   f |              30  |    <!-- not sure, ask Célia -->
|  25-05-17 |            11 | R72B03-GAL4 |    UAS-dTrpA1|              3dd|            V |   f |              30  |    <!-- not sure, ask Célia -->
|  25-05-17 |            12 | empty-GAL4  |    UAS-dTrpA1|              3dd|            V |   f |              30  |    <!-- not sure, ask Célia -->
| 26-05-17  |            01 | TH-C4-GAL4  |    UAS-dTrpA1|               FF|            V |   f |            22    |
| 26-05-17  |            02 | TH-C'-GAL4  |    UAS-dTrpA1|               FF|            V |   f |            22    |
| 26-05-17  |            03 | TH-D1-GAL4  |    UAS-dTrpA1|               FF|            V |   f |            22    |
| 26-05-17  |            04 | TH-D4-GAL4  |    UAS-dTrpA1|               FF|            V |   f |            22    |
| 26-05-17  |            05 | TH-D'-GAL4  |    UAS-dTrpA1|               FF|            V |   f |            22    |
| 26-05-17  |            06 | empty-GAL4  |    UAS-dTrpA1|               FF|            V |   f |            22    |
| 26-05-17  |            07 | R70G12-GAL4 |    UAS-dTrpA1|               FF|            V |   f |              30  |    <!-- not sure, ask Célia -->
| 26-05-17  |            08 | R72B03-GAL4 |    UAS-dTrpA1|               FF|            V |   f |              30  |    <!-- not sure, ask Célia -->
| 26-05-17  |            09 | empty-GAL4  |    UAS-dTrpA1|               FF|            V |   f |              30  |    <!-- not sure, ask Célia -->
| 26-05-17  |            10 | R70G12-GAL4 |    UAS-dTrpA1|              3dd|            V |   f |              30  |    <!-- not sure, ask Célia -->
| 26-05-17  |            11 | R72B03-GAL4 |    UAS-dTrpA1|              3dd|            V |   f |              30  |    <!-- not sure, ask Célia -->
| 26-05-17  |            12 | empty-GAL4  |    UAS-dTrpA1|              3dd|            V |   f |              30  |    <!-- not sure, ask Célia -->

### Group B:
###### Plan: [Google Spreadsheet](https://docs.google.com/a/neuro.fchampalimaud.org/spreadsheets/d/1Ap8V4-8F9u5lc12qadjP3HqXkvDEtwfpO73Tl2NpQQs/edit?usp=sharing)

|    Date | Condition No. | GAL4 driver | UAS effector | Metabolic state | Mating state | Sex | Temperature (ºC) |
|    ---- | ------------- | ----------- | ------------ | --------------- | ------------ | --- | ---------------- |
| 04-08-17|            01 | WED1-GAL4   |    UAS-dTrpA1|                ?|             ?|    ?|               30 | <!-- Males and virgin females -->
| 04-08-17|            02 | R75B10-GAL4 |    UAS-dTrpA1|              FF |           NA |   m |               30 |
| 04-08-17|            03 | R70G12-GAL4 |    UAS-dTrpA1|              FF |           NA |   m |               30 |
| 04-08-17|            04 | R72B03-GAL4 |    UAS-dTrpA1|              FF |           NA |   m |               30 |
| 04-08-17|            05 | R32A06-GAL4 |    UAS-dTrpA1|              FF |           NA |   m |               30 |
| 04-08-17|            06 | empty-GAL4  |    UAS-dTrpA1|              FF |           NA |   m |               30 |


## Substrates:
* channel 1: 10% yeast
* channel 2: 20 mM sucrose

## File structure:
This file tree only contains raw and meta data used for analysis (no duplicates).

* "raw"
    * "04.08.2017 TH TrpA1 males FF 30C"
        * "Result TH TrpA1"
            * CapacitanceData_C01_01_10_C02_11_20_C03_21_30_C04_31_40_C05_41_50_C06_51_602017-08-04T14_12_27.9990016+01_00
            * CapacitanceData_C01_01_10_C02_11_20_C03_21_30_C04_31_40_C05_41_50_C06_51_602017-08-04T15_32_49.8396160+01_00
            * CapacitanceData_C01_01_10_C02_11_20_C03_21_30_C04_31_40_C05_41_50_C06_51_602017-08-04T17_18_44.5750144+01_00
            * CapacitanceData_C01_01_10_C02_11_20_C03_21_30_C04_31_40_C05_41_50_C06_51_602017-08-04T17_30_29.8093056+01_00
            * CapacitanceData_C01_01_10_C02_11_20_C03_21_30_C04_31_40_C05_41_50_C06_51_602017-08-04T17_37_50.1610880+01_00
            * CapacitanceData_C01_01_10_C02_11_22_C03_23_32_C04_33_42_C05_43_52_C06_53_622017-08-04T17_10_57.7452160+01_00
        * '20170804 TH TrpA1.txt'
    * "24.05.2017 Wu TrpA1"
        * "Results"
            * 'CapacitanceData_C01_01_10_C02_11_20_C03_21_30_C04_31_40_C05_41_50_C06_51_602017-05-24T12_52_38'
            * 'CapacitanceData_C01_01_10_C02_11_20_C03_21_30_C04_31_40_C05_41_50_C06_51_602017-05-24T12_56_55'
            * 'CapacitanceData_C01_01_10_C02_11_20_C03_21_30_C04_31_40_C05_41_50_C06_51_602017-05-24T14_20_14'
            * 'CapacitanceData_C01_01_10_C02_11_20_C03_21_30_C04_31_40_C05_41_50_C06_51_602017-05-24T14_24_22'
            * 'CapacitanceData_C01_01_10_C02_11_22_C03_23_32_C04_33_42_C05_43_52_C06_53_622017-05-24T13_02_00.5562496+01_00'
            * 'CapacitanceData_C01_01_10_C02_11_22_C03_23_32_C04_33_42_C05_43_52_C06_53_622017-05-24T14_29_29.5386880+01_00'
            * 'CapacitanceData_C07_01_10_C08_11_20_C09_21_30_C10_31_40_C11_41_50_C12_51_602017-05-24T16_22_23'
            * 'CapacitanceData_C07_01_10_C08_11_20_C09_21_30_C10_31_40_C11_41_50_C12_51_602017-05-24T16_27_35'
            * 'CapacitanceData_C07_01_10_C08_11_20_C09_21_30_C10_31_40_C11_41_50_C12_51_602017-05-24T17_43_26'
            * 'CapacitanceData_C07_01_10_C08_11_20_C09_21_30_C10_31_40_C11_41_50_C12_51_602017-05-24T17_50_45'
            * 'CapacitanceData_C07_01_10_C08_11_22_C09_23_32_C10_33_42_C11_43_52_C12_53_622017-05-24T16_26_00.8441088+01_00'
            * 'CapacitanceData_C07_01_10_C08_11_22_C09_23_32_C10_33_42_C11_43_52_C12_53_622017-05-24T17_57_29.6299264+01_00'
        * '24.05.2017.rtf'
    * "25.05.2017 TH TrpA1 virgins"
        * "Results"
            * 'CapacitanceData_C01_01_10_C02_11_20_C03_21_30_C04_31_40_C05_41_50_C06_51_602017-05-25T12_15_12'
            * 'CapacitanceData_C01_01_10_C02_11_20_C03_21_30_C04_31_40_C05_41_50_C06_51_602017-05-25T12_23_37'
            * 'CapacitanceData_C01_01_10_C02_11_20_C03_21_30_C04_31_40_C05_41_50_C06_51_602017-05-25T13_49_00'
            * 'CapacitanceData_C01_01_10_C02_11_20_C03_21_30_C04_31_40_C05_41_50_C06_51_602017-05-25T13_59_29'
            * 'CapacitanceData_C01_01_10_C02_11_22_C03_23_32_C04_33_42_C05_43_52_C06_53_622017-05-25T12_06_01.3128704+01_00'
            * 'CapacitanceData_C01_01_10_C02_11_22_C03_23_32_C04_33_42_C05_43_52_C06_53_622017-05-25T13_35_56.0627712+01_00'
            * 'CapacitanceData_C07_01_10_C08_11_20_C09_21_30_C10_31_40_C11_41_50_C12_51_602017-05-25T16_08_26'
            * 'CapacitanceData_C07_01_10_C08_11_20_C09_21_30_C10_31_40_C11_41_50_C12_51_602017-05-25T16_15_29'
            * 'CapacitanceData_C07_01_10_C08_11_22_C09_23_32_C10_33_44_C11_45_54_C12_55_642017-05-25T15_57_21.5115392+01_00'
            * 'CapacitanceData_C07_01_10_C08_11_22_C09_23_32_C10_33_44_C11_45_54_C12_55_642017-05-25T17_09_40.5904128+01_00'
            * 'CapacitanceData_C07_01_10_C09_21_30_C10_31_40_C11_41_50_C12_51_602017-05-25T17_22_28'
            * 'CapacitanceData_C07_01_10_C09_21_30_C10_31_40_C11_41_50_C12_51_602017-05-25T17_31_36'
        * '25.05.2017.rtf'
    * "26.05.2017 TH TrpA1 males"
        * "Results"
            * 'CapacitanceData_C01_01_10_C02_11_20_C03_21_30_C04_31_40_C05_41_50_C06_51_602017-05-26T15_01_22'
            * 'CapacitanceData_C01_01_10_C02_11_20_C03_21_30_C04_31_40_C05_41_50_C06_51_602017-05-26T15_16_05'
            * 'CapacitanceData_C01_01_10_C02_11_20_C03_21_30_C04_31_40_C05_41_50_C06_51_602017-05-26T16_11_32'
            * 'CapacitanceData_C01_01_10_C02_11_20_C03_21_30_C04_31_40_C05_41_50_C06_51_602017-05-26T16_25_36'
            * 'CapacitanceData_C01_01_10_C02_11_22_C03_23_32_C04_33_42_C05_43_52_C06_53_622017-05-26T14_43_14.7235584+01_00'
            * 'CapacitanceData_C01_01_10_C02_11_22_C03_23_32_C04_33_42_C05_43_52_C06_53_622017-05-26T15_59_45.0038400+01_00'
            * 'CapacitanceData_C07_01_10_C08_11_20_C09_21_30_C10_31_40_C11_41_50_C12_51_602017-05-26T17_39_37'
            * 'CapacitanceData_C07_01_10_C08_11_20_C09_21_30_C10_31_40_C11_41_50_C12_51_602017-05-26T17_47_20'
            * 'CapacitanceData_C07_01_10_C08_11_20_C09_21_30_C10_31_40_C11_41_50_C12_51_602017-05-26T19_00_54'
            * 'CapacitanceData_C07_01_10_C08_11_20_C09_21_30_C10_31_40_C11_41_50_C12_51_602017-05-26T19_09_03'
            * 'CapacitanceData_C07_01_10_C08_11_22_C09_23_32_C10_33_42_C11_43_52_C12_53_622017-05-26T17_33_54.3538304+01_00'
            * 'CapacitanceData_C07_01_10_C08_11_22_C09_23_32_C10_33_42_C11_43_52_C12_53_622017-05-26T18_46_44.9723904+01_00'
        * '25.05.2017.rtf'
* 'README.md'

## Sessions metadata:
The sessions metadata (mapping files-metadata)

## Results:

## Discussion:

## References:
* Liu Q, Tabuchi M, Liu S, Kodama L, Horiuchi W, Daniels J, Chiu L, Baldoni D, Wu MN. Branch-specific plasticity of a bifunctional dopamine circuit encodes protein hunger. Science. 2017 May 5;356(6337):534-9.
