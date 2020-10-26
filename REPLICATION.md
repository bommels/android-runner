# MobileSoft 2021 - Native app vs their web app counterpart, which one consumes more? – Replication package


This repository contains the replication package and dataset of the paper with the title **Native app vs their web app counterpart, which one consumes more?**.

This study has been designed, developed, and reported by the following investigators:

- Luciën Martijn (Vrije Universiteit Amsterdam)
- Stijn Meijerink (Vrije Universiteit Amsterdam)
- Dion David Haneveld (Vrije Universiteit Amsterdam)
- Daniël Hana (Vrije Universiteit Amsterdam)
- Terry Bommels (Vrije Universiteit Amsterdam)

For any information, interested researchers can contact us by sending an email to any of the investigators listed above.
The full dataset including raw data, mining scripts, and analysis scripts produced during the study are available below.

## How to cite this study
If this study is helping your research, consider to cite it is as follows, thanks!

```
@inproceedings{MobileSoft2021,
  title={{Native app vs their web app counterpart, which one consumes more?}},
  author={Luciën Martijn and Stijn Meijerink and Dion David Haneveld Daniël Hana and Terry Bommels},
  booktitle = {Proceedings of the 8th IEEE/ACM International Conference on Mobile Software Engineering and Systems},
  year = {2021},
  pages = {to appear},
  numpages = {11}
}
```

### Overview of the replication package
---

This replication package is structured as follows:

```
    android-runner
    .
    |--- experiments/                          The monkeyrunner scripts with JSON configuration files for each device type and app type
    |
    |--- DataProcessing/clean_pipeline.Rmd     The R Markdown file for plotting and assessing the extracted data (see below).
    |
    |--- DataProcessing/Data/                  The full dataset used in the paper.    
    |
    |--- mobilesoft-2021-nativevsweb.pdf       A copy of the paper in pdf format
    
```

Each of the folders listed above are described in details in the remaining of this readme.

### experiments/
---
```
    experiments
    .
    |--- apps/                        All the APKs and XAPKs of the native apps
    |
    |--- power_profile/               Contains power_profile.xml of both low-end and high-end device                  
    |
    |--- scripts/                     monkeyrunner scripts of each device type and app type
    |
    |--- config_7pro_native.json      android-runner configuration file for batterystats for native apps on high-end device
    |
    |--- config_7pro_web.json         android-runner configuration file for batterystats for web apps on high-end device
    |
    |--- config_J7_native.json        android-runner configuration file for batterystats for native apps on low-end device
    |
    |--- config_J7_web.json           android-runner configuration file for batterystats for web apps on low-end device
```

### DataProcessing/
---
```
    DataProcessing
    .
    |--- plots/                       Plot figures
    |
    |--- all_results.csv              Entire dataset
    |
    |--- data_pipeline.Rmd            R script for plotting and assesing the dataset
    |
    |--- data_pipeline.pdf            Output of R Markdown file in pdf format
```

### DataProcessing/Data/
---
```
    Data
    .
    |--- high.end.native/      The raw measurement batterystats output files of each native app on high end device.  
    |--- high.end.web/         The raw measurement batterystats output files of each web app on high end device.  
    |--- low.end.native/       The raw measurement batterystats output files of each native app on low end device.  
    |--- low.end.web/          The raw measurement batterystats output files of each web app on low end device.  

``` 


## License

This software is licensed under the MIT License.
