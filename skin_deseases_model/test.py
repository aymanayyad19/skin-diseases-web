
# To Load Model

from keras._tf_keras.keras.models import load_model

mmmmm = load_model("filename.h5")

# to use the model for predict
#
# mmmmm.predict("image file")
#
#
# labels_dict = {'Acne and Rosacea':0,'Actinic Keratosis Basal Cell Carcinoma and other Malignant Lesions':1,'Atopic Dermatitis':2
#              ,'Bullous Disease' : 3 , 'Cellulitis Impetigo and other Bacterial Infections' : 4 ,'Eczema': 5,'Exanthems and Drug Eruptions':6 ,'Hair Loss Photos Alopecia and other Hair Diseases': 7 ,'Herpes HPV and other STDs': 8,
#                'Light Diseases and Disorders of Pigmentation':9 ,'Lupus and other Connective Tissue diseases' : 10 ,
#                'Melanoma Skin Cancer Nevi and Moles' : 11 , 'Nail Fungus and other Nail Disease' : 12,
#                'Poison Ivy Photos and other Contact Dermatitis':13,'Psoriasis pictures Lichen Planus and related diseases':14,
#                'Scabies Lyme Disease and other Infestations and Bites' : 15 ,'Seborrheic Keratoses and other Benign Tumors' : 16 ,
#                'Systemic Disease' : 17,'Tinea Ringworm Candidiasis and other Fungal Infections': 18,
#                'Urticaria Hives' : 19 , 'Vascular Tumors': 20 ,'Vasculitis': 21,'Warts Molluscum and other Viral Infections':22}

               