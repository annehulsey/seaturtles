"""
 Loads the constants from the the underlying model

 Documentation is provided in the following document:
      Markhvida, M., Ceferino, L., and Baker, J. W. (2018), “Modeling spatially correlated
      spectral accelerations at multiple periods using principal component analysis and geostatistics.”
      Earthquake Engineering & Structural Dynamics, 47(5), 1107–1123.

 The data can also be viewed in the files included in the TURtLES package:
    Markhvida_variogram.json: json file
        Dictionary of the underlying semivariogram models
        Created based on Table 2 from the paper's electronic supplement

    Markhvida_Table_1.csv: csv file
        Coefficients for transforming the principal components to spectral accelerations
        Table 1 from the paper's electronic supplement

"""

from .base import *

pca_variogram = {'PC1': [{'Type': 'isotropic_nested_covariance',
               'co': 2.5,
               'c1': 4.52,
               'a1': 15,
               'c2': 6.78,
               'a2': 250}],
             'PC2': [{'Type': 'isotropic_nested_covariance',
               'co': 0.5,
               'c1': 1.4,
               'a1': 10,
               'c2': 2.6,
               'a2': 160}],
             'PC3': [{'Type': 'isotropic_nested_covariance',
               'co': 0.15,
               'c1': 0.42,
               'a1': 15,
               'c2': 0.63,
               'a2': 160}],
             'PC4': [{'Type': 'isotropic_nested_covariance',
               'co': 0.15,
               'c1': 0.225,
               'a1': 10,
               'c2': 0.225,
               'a2': 120}],
             'PC5': [{'Type': 'nugget_covariance', 'co': 0.314321867}],
             'PC6': [{'Type': 'nugget_covariance', 'co': 0.190749536}],
             'PC7': [{'Type': 'nugget_covariance', 'co': 0.137846759}],
             'PC8': [{'Type': 'nugget_covariance', 'co': 0.111283843}],
             'PC9': [{'Type': 'nugget_covariance', 'co': 0.096499281}],
             'PC10': [{'Type': 'nugget_covariance', 'co': 0.071736797}],
             'PC11': [{'Type': 'nugget_covariance', 'co': 0.064816215}],
             'PC12': [{'Type': 'nugget_covariance', 'co': 0.054076636}],
             'PC13': [{'Type': 'nugget_covariance', 'co': 0.051188751}],
             'PC14': [{'Type': 'nugget_covariance', 'co': 0.04331642}],
             'PC15': [{'Type': 'nugget_covariance', 'co': 0.041398046}],
             'PC16': [{'Type': 'nugget_covariance', 'co': 0.034663672}],
             'PC17': [{'Type': 'nugget_covariance', 'co': 0.018796994}],
             'PC18': [{'Type': 'nugget_covariance', 'co': 0.002856941}],
             'PC19': [{'Type': 'nugget_covariance', 'co': 0.000360645}]}

pca_periods = np.array([0.01 , 0.02 , 0.03 , 0.05 , 0.075, 0.1  , 0.15 , 0.2  , 0.25 ,
                   0.3  , 0.4  , 0.5  , 0.75 , 1.   , 1.5  , 2.   , 3.   , 4.   ,
                   5.   ])

pca_coefficients = np.array([[ 2.70963956e-01, -1.39418157e-01,  6.90420060e-02,
                        -1.06094866e-01, -9.22880750e-02, -1.13489976e-01,
                        -1.88935371e-01,  1.53956802e-01, -1.60082932e-01,
                        -4.85878660e-02,  1.06169114e-01,  5.45367130e-02,
                        -8.42347290e-02,  2.06507200e-03,  2.33666516e-01,
                        -4.44106080e-02, -2.98766213e-01, -5.27588860e-01,
                        -5.80349073e-01],
                       [ 2.70185457e-01, -1.41734439e-01,  7.70156690e-02,
                        -1.16393534e-01, -1.03464378e-01, -1.24082463e-01,
                        -1.99840301e-01,  1.55452551e-01, -1.57024101e-01,
                        -5.11781530e-02,  1.02685985e-01,  5.34091780e-02,
                        -7.85807730e-02,  5.38047500e-03,  2.20317829e-01,
                        -3.94525930e-02, -2.57172669e-01, -1.50994889e-01,
                         7.81868928e-01],
                       [ 2.66716484e-01, -1.50918021e-01,  1.01241750e-01,
                        -1.44620230e-01, -1.28327845e-01, -1.50413273e-01,
                        -2.17519115e-01,  1.54533128e-01, -1.44555133e-01,
                        -4.93784910e-02,  8.65380810e-02,  3.69034470e-02,
                        -5.51975900e-02,  7.87249500e-03,  1.49651510e-01,
                        -2.32087970e-02, -2.84597880e-02,  8.08901724e-01,
                        -2.26437335e-01],
                       [ 2.51688240e-01, -1.84642999e-01,  1.78879968e-01,
                        -2.21328311e-01, -1.75557526e-01, -1.76668887e-01,
                        -1.88651351e-01,  4.24749060e-02, -4.55090100e-02,
                        -2.91885730e-02, -3.15764520e-02, -6.05411450e-02,
                         9.35508240e-02,  2.24423930e-02, -2.99181352e-01,
                         5.99168860e-02,  7.54350403e-01, -2.06472973e-01,
                         2.31093450e-02],
                       [ 2.36434541e-01, -2.18922079e-01,  2.37254184e-01,
                        -2.34559034e-01, -1.33267088e-01, -4.31828090e-02,
                         1.19447151e-01, -2.72310555e-01,  2.38192698e-01,
                         1.00676333e-01, -2.63315034e-01, -1.21207177e-01,
                         2.02769694e-01,  6.61936100e-03, -4.93306767e-01,
                         1.16246173e-01, -4.75923823e-01,  3.67733770e-02,
                        -6.43955700e-03],
                       [ 2.32994643e-01, -2.28087987e-01,  2.30554573e-01,
                        -1.60443024e-01,  4.00564220e-02,  1.81657485e-01,
                         4.27112684e-01, -3.24579280e-01,  2.63780433e-01,
                         1.42634796e-01, -8.13780350e-02,  4.65305510e-02,
                        -1.51801547e-01, -8.33183140e-02,  5.34198178e-01,
                        -1.84596750e-01,  2.10357917e-01, -2.84225600e-03,
                         3.31108700e-03],
                       [ 2.38919759e-01, -2.11905954e-01,  1.32646222e-01,
                         8.20453500e-02,  3.27946973e-01,  3.93273105e-01,
                         3.25836316e-01,  1.62029625e-01, -1.82164846e-01,
                        -1.38319895e-01,  4.70111475e-01,  1.77876088e-01,
                        -1.11256500e-01,  8.83177910e-02, -2.91143253e-01,
                         2.62494245e-01, -1.52291500e-03,  1.54770020e-02,
                         1.50080900e-03],
                       [ 2.47247201e-01, -1.74053610e-01, -8.25743300e-03,
                         2.77382297e-01,  4.03271334e-01,  2.20437620e-01,
                        -8.37312940e-02,  2.24796020e-01, -1.71941473e-01,
                        -2.92747130e-02, -3.81524121e-01, -2.37244496e-01,
                         3.56271009e-01, -8.50495000e-02, -1.25434810e-02,
                        -4.42559355e-01,  1.51125190e-02,  1.10964550e-02,
                         1.94187500e-03],
                       [ 2.53677097e-01, -1.22375885e-01, -1.48595586e-01,
                         3.65271223e-01,  2.53186444e-01, -6.12442510e-02,
                        -2.83389735e-01, -8.11437930e-02,  2.12210668e-01,
                         1.43362427e-01, -2.75727619e-01, -4.11307160e-02,
                        -2.02014525e-01,  2.28459040e-02,  1.55257214e-01,
                         6.32145332e-01,  4.55130190e-02,  6.91000000e-04,
                         4.70000000e-04],
                       [ 2.54921192e-01, -7.13194460e-02, -2.37030888e-01,
                         3.59073100e-01,  4.01080110e-02, -2.48766602e-01,
                        -1.41859038e-01, -2.86692239e-01,  3.00971238e-01,
                         5.79993720e-02,  3.28411992e-01,  2.08361703e-01,
                        -1.94768508e-01,  3.24295010e-02, -2.58822161e-01,
                        -4.77244327e-01,  1.91094700e-03,  6.62185300e-03,
                         1.88000000e-04],
                       [ 2.52458254e-01,  1.25091290e-02, -3.27121081e-01,
                         2.26053197e-01, -2.61297620e-01, -2.16236975e-01,
                         3.44080560e-01, -1.21230621e-01, -6.02714320e-02,
                        -2.19189671e-01,  2.11470671e-01, -1.28634841e-01,
                         5.76234521e-01, -5.50760430e-02,  1.97333044e-01,
                         2.05766455e-01,  2.36621450e-02,  3.70370100e-03,
                         1.85000000e-04],
                       [ 2.45944241e-01,  7.99604140e-02, -3.58449873e-01,
                         6.40998100e-02, -3.41792254e-01,  2.24967550e-02,
                         3.88717982e-01,  1.77122204e-01, -2.55990758e-01,
                        -6.44303600e-03, -3.75390123e-01, -7.62061470e-02,
                        -5.02002036e-01,  1.83662360e-02, -1.76351452e-01,
                        -6.86345490e-02,  1.54233460e-02,  5.41822800e-03,
                         1.27868900e-03],
                       [ 2.25758567e-01,  1.91381035e-01, -3.35176303e-01,
                        -2.16152634e-01, -1.65178955e-01,  4.23011572e-01,
                        -1.44255462e-01,  1.87567292e-01,  1.49360082e-01,
                         5.30105301e-01,  4.17962320e-02,  3.26784764e-01,
                         2.74609836e-01,  5.58724760e-02,  4.42737600e-03,
                         1.11352500e-02,  2.44045340e-02,  6.83000000e-04,
                         1.99000000e-04],
                       [ 2.11097169e-01,  2.59405650e-01, -2.43643585e-01,
                        -3.25745719e-01,  7.63484290e-02,  3.30279571e-01,
                        -2.20001696e-01, -1.17395307e-01,  2.71296591e-01,
                        -4.38774328e-01,  1.48165306e-01, -4.84545679e-01,
                        -1.43691434e-01, -3.89147470e-02,  8.93381600e-03,
                        -2.05549230e-02, -6.11584400e-03,  3.80246500e-03,
                        -3.89000000e-04],
                       [ 1.88387437e-01,  3.29799741e-01, -9.46692610e-02,
                        -2.73646379e-01,  3.56651426e-01, -1.53161130e-01,
                        -6.82000000e-04, -3.29897663e-01, -2.67361750e-01,
                        -2.79382156e-01, -2.63740501e-01,  5.28987613e-01,
                         7.03281460e-02, -8.35258440e-02, -2.54953440e-02,
                         2.71139320e-02,  1.26194670e-02,  3.85357400e-03,
                        -8.10000000e-04],
                       [ 1.76395533e-01,  3.57332294e-01,  5.54387510e-02,
                        -1.55161958e-01,  3.54513035e-01, -3.43041979e-01,
                         1.61895880e-01, -2.75355960e-02, -2.07859409e-01,
                         5.06833313e-01,  2.05450556e-01, -4.13916086e-01,
                        -4.07497250e-02,  1.68472841e-01, -2.35465700e-03,
                        -5.88317600e-03, -3.34222400e-03,  1.97868700e-03,
                         1.70392000e-03],
                       [ 1.65469018e-01,  3.60040620e-01,  2.60392170e-01,
                         6.69803670e-02,  5.72701980e-02, -2.20913199e-01,
                         1.81062550e-01,  5.19913777e-01,  4.62086625e-01,
                        -1.04489885e-01, -2.19632040e-02,  1.19011799e-01,
                        -4.29988200e-03, -4.17545575e-01, -4.01081050e-02,
                         2.00607200e-02, -5.26025200e-03, -5.80167400e-03,
                         4.58000000e-04],
                       [ 1.59580892e-01,  3.47927160e-01,  3.48346295e-01,
                         2.39394141e-01, -1.57211928e-01,  9.28779110e-02,
                        -5.01602100e-03,  1.69759690e-02,  1.09978222e-01,
                        -1.82603154e-01, -1.21233490e-01,  7.11306930e-02,
                         6.20582730e-02,  7.50450107e-01,  7.85420660e-02,
                        -5.21102090e-02,  7.51936600e-03, -1.88268100e-03,
                        -1.85190400e-03],
                       [ 1.48832921e-01,  3.32847695e-01,  3.65098052e-01,
                         3.31227695e-01, -2.81334582e-01,  2.83334016e-01,
                        -1.82848345e-01, -3.25817997e-01, -3.10946154e-01,
                         1.28556114e-01,  8.37173660e-02, -7.03828760e-02,
                        -4.61924130e-02, -4.41499964e-01, -4.05906260e-02,
                         3.37161620e-02,  1.16291900e-03,  4.01605000e-03,
                         5.06000000e-04]])

pca_variance_explained = np.array([0.63984175, 0.84627714, 0.90453306, 0.93340282, 0.95015459,
                               0.96046156, 0.96797214, 0.9738782 , 0.97929703, 0.9833458 ,
                               0.98663949, 0.9896814 , 0.99236758, 0.99479044, 0.99692908,
                               0.99875974, 0.99976488, 0.99996981, 1.        ])