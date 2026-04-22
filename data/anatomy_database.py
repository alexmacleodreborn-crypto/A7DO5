"""
A7DO Anatomy Database
Contains all anatomical data extracted from the provided data files
"""

# Layer 01: Bones (Skeletal System)
BONES = {
    # Axial Skeleton
    "skull": {
        "id": 1,
        "name": "Skull (Cranium)",
        "category": "axial",
        "subcategories": ["frontal", "parietal", "temporal", "occipital", "sphenoid", "ethmoid"],
        "articulations": ["mandible", "cervical_vertebrae"],
        "growth_stages": {
            "birth": {"weight_g": 100, "description": "Fontanelles present"},
            "10_years": {"weight_g": 200, "description": "Fontanelles closed"},
            "adulthood": {"weight_g": 250, "description": "Fully fused"}
        }
    },
    "mandible": {
        "id": 2,
        "name": "Mandible",
        "category": "axial",
        "articulations": ["skull"],
        "muscle_attachments": ["masseter", "temporalis", "pterygoids"]
    },
    "cervical_vertebrae": {
        "id": 3,
        "name": "Cervical Vertebrae",
        "category": "axial",
        "count": 7,
        "labels": ["C1 (Atlas)", "C2 (Axis)", "C3", "C4", "C5", "C6", "C7"],
        "articulations": ["skull", "thoracic_vertebrae"]
    },
    "thoracic_vertebrae": {
        "id": 4,
        "name": "Thoracic Vertebrae",
        "category": "axial",
        "count": 12,
        "articulations": ["cervical_vertebrae", "lumbar_vertebrae", "ribs"]
    },
    "lumbar_vertebrae": {
        "id": 5,
        "name": "Lumbar Vertebrae",
        "category": "axial",
        "count": 5,
        "articulations": ["thoracic_vertebrae", "sacrum"]
    },
    "sacrum": {
        "id": 6,
        "name": "Sacrum",
        "category": "axial",
        "fused_vertebrae": 5,
        "articulations": ["lumbar_vertebrae", "coccyx", "pelvis"]
    },
    "coccyx": {
        "id": 7,
        "name": "Coccyx (Tailbone)",
        "category": "axial",
        "fused_vertebrae": 4,
        "articulations": ["sacrum"]
    },
    "ribs": {
        "id": 8,
        "name": "Ribs",
        "category": "axial",
        "count": 24,
        "types": ["true_ribs (1-7)", "false_ribs (8-10)", "floating_ribs (11-12)"],
        "articulations": ["thoracic_vertebrae", "sternum"]
    },
    "sternum": {
        "id": 9,
        "name": "Sternum (Breastbone)",
        "category": "axial",
        "parts": ["manubrium", "body", "xiphoid_process"],
        "articulations": ["clavicle", "ribs"]
    },
    # Appendicular Skeleton - Upper Limbs
    "clavicle": {
        "id": 10,
        "name": "Clavicle (Collarbone)",
        "category": "appendicular_upper",
        "side": "bilateral",
        "articulations": ["sternum", "scapula"],
        "growth_stages": {
            "birth": {"length_cm": 4, "description": "Medial epiphysis cartilaginous"},
            "10_years": {"length_cm": 8, "description": "Actively growing"},
            "adulthood": {"length_cm": 15, "description": "Fully ossified"}
        }
    },
    "scapula": {
        "id": 11,
        "name": "Scapula (Shoulder Blade)",
        "category": "appendicular_upper",
        "side": "bilateral",
        "articulations": ["clavicle", "humerus"],
        "muscle_attachments": ["deltoid", "trapezius", "rotator_cuff"]
    },
    "left_humerus": {
        "id": 85,
        "name": "Left Humerus",
        "category": "appendicular_upper",
        "type": "long_bone",
        "articulations": ["scapula", "radius", "ulna"],
        "growth_stages": {
            "birth": {"length_cm": 6.5, "width_cm": 1.2, "circumference_cm": 3.5, "weight_g": 20},
            "10_years": {"length_cm": 22, "width_cm": 1.8, "circumference_cm": 6, "weight_g": 90},
            "adulthood": {"length_cm": 33, "width_cm": 2.5, "circumference_cm": 7.5, "weight_g": 150}
        }
    },
    "right_humerus": {
        "id": 86,
        "name": "Right Humerus",
        "category": "appendicular_upper",
        "type": "long_bone",
        "articulations": ["scapula", "radius", "ulna"]
    },
    "radius": {
        "id": 12,
        "name": "Radius",
        "category": "appendicular_upper",
        "side": "bilateral",
        "type": "long_bone",
        "articulations": ["humerus", "ulna", "carpals"]
    },
    "ulna": {
        "id": 13,
        "name": "Ulna",
        "category": "appendicular_upper",
        "side": "bilateral",
        "type": "long_bone",
        "articulations": ["humerus", "radius", "carpals"]
    },
    "carpals": {
        "id": 14,
        "name": "Carpal Bones",
        "category": "appendicular_upper",
        "count": 8,
        "bones": ["scaphoid", "lunate", "triquetrum", "pisiform", "trapezium", "trapezoid", "capitate", "hamate"]
    },
    "metacarpals": {
        "id": 15,
        "name": "Metacarpal Bones",
        "category": "appendicular_upper",
        "count": 5,
        "articulations": ["carpals", "phalanges"]
    },
    "phalanges_hand": {
        "id": 16,
        "name": "Phalanges (Hand)",
        "category": "appendicular_upper",
        "count": 14,
        "distribution": {"thumb": 2, "fingers": 3}
    },
    # Appendicular Skeleton - Lower Limbs
    "pelvis": {
        "id": 17,
        "name": "Pelvis (Hip Bone)",
        "category": "appendicular_lower",
        "components": ["ilium", "ischium", "pubis"],
        "articulations": ["sacrum", "femur"]
    },
    "left_femur": {
        "id": 147,
        "name": "Left Femur",
        "category": "appendicular_lower",
        "type": "long_bone",
        "is_longest_bone": True,
        "articulations": ["pelvis", "tibia", "patella"],
        "growth_stages": {
            "birth": {"length_cm": 8, "width_cm": 1.5, "circumference_cm": 4, "weight_g": 30},
            "10_years": {"length_cm": 30, "width_cm": 2.2, "circumference_cm": 7, "weight_g": 150},
            "adulthood": {"length_cm": 45, "width_cm": 3, "circumference_cm": 9, "weight_g": 290}
        }
    },
    "right_femur": {
        "id": 148,
        "name": "Right Femur",
        "category": "appendicular_lower",
        "type": "long_bone",
        "is_longest_bone": True,
        "articulations": ["pelvis", "tibia", "patella"]
    },
    "patella": {
        "id": 18,
        "name": "Patella (Kneecap)",
        "category": "appendicular_lower",
        "side": "bilateral",
        "type": "sesamoid_bone"
    },
    "tibia": {
        "id": 19,
        "name": "Tibia (Shinbone)",
        "category": "appendicular_lower",
        "side": "bilateral",
        "type": "long_bone",
        "articulations": ["femur", "fibula", "talus"]
    },
    "fibula": {
        "id": 20,
        "name": "Fibula",
        "category": "appendicular_lower",
        "side": "bilateral",
        "type": "long_bone",
        "articulations": ["tibia", "talus"]
    },
    "tarsals": {
        "id": 21,
        "name": "Tarsal Bones",
        "category": "appendicular_lower",
        "count": 7,
        "bones": ["calcaneus", "talus", "navicular", "cuboid", "medial_cuneiform", "intermediate_cuneiform", "lateral_cuneiform"]
    },
    "metatarsals": {
        "id": 22,
        "name": "Metatarsal Bones",
        "category": "appendicular_lower",
        "count": 5,
        "articulations": ["tarsals", "phalanges"]
    },
    "phalanges_foot": {
        "id": 23,
        "name": "Phalanges (Foot)",
        "category": "appendicular_lower",
        "count": 14,
        "distribution": {"great_toe": 2, "toes": 3}
    }
}

# Layer 02: Muscles (Muscular System)
MUSCLES = {
    # Head and Neck
    "frontalis": {
        "id": 1,
        "name": "Frontalis",
        "group": "facial_expression",
        "origin": "galea_aponeurotica",
        "insertion": "skin_of_forehead",
        "action": "raises_eyebrows",
        "innervation": "facial_nerve_cn_vii"
    },
    "occipitalis": {
        "id": 2,
        "name": "Occipitalis",
        "group": "facial_expression",
        "origin": "occipital_bone",
        "insertion": "galea_aponeurotica",
        "action": "moves_scalp_back",
        "innervation": "facial_nerve_cn_vii"
    },
    "orbicularis_oculi": {
        "id": 3,
        "name": "Orbicularis Oculi",
        "group": "facial_expression",
        "action": "closes_eye",
        "innervation": "facial_nerve_cn_vii"
    },
    "orbicularis_oris": {
        "id": 4,
        "name": "Orbicularis Oris",
        "group": "facial_expression",
        "action": "closes_lips",
        "innervation": "facial_nerve_cn_vii"
    },
    "masseter": {
        "id": 5,
        "name": "Masseter",
        "group": "mastication",
        "origin": "zygomatic_arch",
        "insertion": "mandible",
        "action": "closes_jaw",
        "innervation": "trigeminal_nerve_cn_v"
    },
    "temporalis": {
        "id": 6,
        "name": "Temporalis",
        "group": "mastication",
        "origin": "temporal_fossa",
        "insertion": "coronoid_process_of_mandible",
        "action": "closes_jaw",
        "innervation": "trigeminal_nerve_cn_v"
    },
    "sternocleidomastoid": {
        "id": 7,
        "name": "Sternocleidomastoid",
        "group": "neck",
        "origin": ["sternum", "clavicle"],
        "insertion": "mastoid_process",
        "action": "rotates_head",
        "innervation": "accessory_nerve_cn_xi"
    },
    "trapezius": {
        "id": 8,
        "name": "Trapezius",
        "group": "back_superficial",
        "origin": ["occipital_bone", "c7", "thoracic_vertebrae"],
        "insertion": ["clavicle", "acromion", "spine_of_scapula"],
        "action": "elevates_retracts_scapula",
        "innervation": "accessory_nerve_cn_xi"
    },
    # Torso
    "pectoralis_major": {
        "id": 9,
        "name": "Pectoralis Major",
        "group": "chest",
        "origin": ["clavicle", "sternum", "ribs"],
        "insertion": "greater_tubercle_of_humerus",
        "action": "adducts_medially_rotates_arm",
        "innervation": "medial_and_lateral_pterygoid"
    },
    "pectoralis_minor": {
        "id": 10,
        "name": "Pectoralis Minor",
        "group": "chest",
        "origin": "ribs_3-5",
        "insertion": "coracoid_process",
        "action": "depresses_scapula",
        "innervation": "medial_pterygoid"
    },
    "latissimus_dorsi": {
        "id": 11,
        "name": "Latissimus Dorsi",
        "group": "back",
        "origin": ["thoracolumbar_fascia", "iliac_crest"],
        "insertion": "intertubercular_groove_of_humerus",
        "action": "adducts_extends_medially_rotates_arm",
        "innervation": "thoracodorsal_nerve"
    },
    "rectus_abdominis": {
        "id": 22,
        "name": "Rectus Abdominis",
        "group": "abdominal",
        "origin": "pubic_symphysis",
        "insertion": ["xiphoid_process", "costal_cartilages_5-7"],
        "action": "flexes_trunk",
        "innervation": "intercostal_nerves",
        "growth_stages": {
            "birth": {"length_cm": 10, "width_cm": 3, "weight_g": 15},
            "10_years": {"length_cm": 25, "width_cm": 6, "weight_g": 100},
            "adulthood": {"length_cm": 40, "width_cm": 10, "weight_g": 250}
        }
    },
    "external_oblique": {
        "id": 12,
        "name": "External Oblique",
        "group": "abdominal",
        "action": "flexes_rotates_trunk",
        "innervation": "intercostal_nerves"
    },
    "internal_oblique": {
        "id": 13,
        "name": "Internal Oblique",
        "group": "abdominal",
        "action": "flexes_rotates_trunk",
        "innervation": "intercostal_nerves"
    },
    "transversus_abdominis": {
        "id": 14,
        "name": "Transversus Abdominis",
        "group": "abdominal",
        "action": "compresses_abdomen",
        "innervation": "intercostal_nerves"
    },
    "erector_spinae": {
        "id": 15,
        "name": "Erector Spinae",
        "group": "back_deep",
        "components": ["iliocostalis", "longissimus", "spinalis"],
        "action": "extends_spine",
        "innervation": "dorsal_rami"
    },
    # Shoulder and Upper Arm
    "deltoid": {
        "id": 16,
        "name": "Deltoid",
        "group": "shoulder",
        "origin": ["clavicle", "acromion", "spine_of_scapula"],
        "insertion": "deltoid_tuberosity_of_humerus",
        "action": "abducts_arm",
        "innervation": "axillary_nerve"
    },
    "supraspinatus": {
        "id": 17,
        "name": "Supraspinatus",
        "group": "rotator_cuff",
        "origin": "supraspinous_fossa",
        "insertion": "greater_tubercle_of_humerus",
        "action": "abducts_arm",
        "innervation": "suprascapular_nerve"
    },
    "infraspinatus": {
        "id": 18,
        "name": "Infraspinatus",
        "group": "rotator_cuff",
        "origin": "infraspinous_fossa",
        "insertion": "greater_tubercle_of_humerus",
        "action": "laterally_rotates_arm",
        "innervation": "suprascapular_nerve"
    },
    "subscapularis": {
        "id": 19,
        "name": "Subscapularis",
        "group": "rotator_cuff",
        "origin": "subscapular_fossa",
        "insertion": "lesser_tubercle_of_humerus",
        "action": "medially_rotates_arm",
        "innervation": "subscapular_nerves"
    },
    "teres_minor": {
        "id": 20,
        "name": "Teres Minor",
        "group": "rotator_cuff",
        "origin": "lateral_border_of_scapula",
        "insertion": "greater_tubercle_of_humerus",
        "action": "laterally_rotates_arm",
        "innervation": "axillary_nerve"
    },
    "biceps_brachii": {
        "id": 21,
        "name": "Biceps Brachii",
        "group": "upper_arm_anterior",
        "heads": ["long_head", "short_head"],
        "origin": ["supraglenoid_tubercle", "coracoid_process"],
        "insertion": "radial_tuberosity",
        "action": "flexes_elbow_supinates_forearm",
        "innervation": "musculocutaneous_nerve"
    },
    "triceps_brachii": {
        "id": 22,
        "name": "Triceps Brachii",
        "group": "upper_arm_posterior",
        "heads": ["long_head", "lateral_head", "medial_head"],
        "origin": ["infraglenoid_tubercle", "posterior_humerus", "posterior_humerus"],
        "insertion": "olecranon_of_ulna",
        "action": "extends_elbow",
        "innervation": "radial_nerve"
    },
    # Forearm
    "brachialis": {
        "id": 23,
        "name": "Brachialis",
        "group": "upper_arm_anterior",
        "origin": "anterior_humerus",
        "insertion": "coronoid_process_of_ulna",
        "action": "flexes_elbow",
        "innervation": "musculocutaneous_nerve"
    },
    "brachioradialis": {
        "id": 24,
        "name": "Brachioradialis",
        "group": "forearm",
        "action": "flexes_elbow",
        "innervation": "radial_nerve"
    },
    # Hip and Lower Limb
    "gluteus_maximus": {
        "id": 25,
        "name": "Gluteus Maximus",
        "group": "gluteal",
        "origin": ["ilium", "sacrum", "coccyx"],
        "insertion": "gluteal_tuberosity_of_femur",
        "action": "extends_laterally_rotates_thigh",
        "innervation": "inferior_gluteal_nerve"
    },
    "gluteus_medius": {
        "id": 26,
        "name": "Gluteus Medius",
        "group": "gluteal",
        "action": "abducts_medially_rotates_thigh",
        "innervation": "superior_gluteal_nerve"
    },
    "gluteus_minimus": {
        "id": 27,
        "name": "Gluteus Minimus",
        "group": "gluteal",
        "action": "abducts_medially_rotates_thigh",
        "innervation": "superior_gluteal_nerve"
    },
    "iliopsoas": {
        "id": 28,
        "name": "Iliopsoas",
        "group": "hip_flexor",
        "components": ["psoas_major", "iliacus"],
        "action": "flexes_thigh",
        "innervation": "femoral_nerve"
    },
    "quadriceps_femoris": {
        "id": 29,
        "name": "Quadriceps Femoris",
        "group": "thigh_anterior",
        "components": ["rectus_femoris", "vastus_lateralis", "vastus_medialis", "vastus_intermedius"],
        "action": "extends_leg",
        "innervation": "femoral_nerve"
    },
    "hamstrings": {
        "id": 30,
        "name": "Hamstrings",
        "group": "thigh_posterior",
        "components": ["biceps_femoris", "semitendinosus", "semimembranosus"],
        "action": "flexes_leg_extends_thigh",
        "innervation": "sciatic_nerve"
    },
    "adductor_group": {
        "id": 31,
        "name": "Adductor Group",
        "group": "thigh_medial",
        "components": ["adductor_longus", "adductor_brevis", "adductor_magnus", "gracilis", "pectineus"],
        "action": "adducts_thigh",
        "innervation": "obturator_nerve"
    },
    "gastrocnemius": {
        "id": 32,
        "name": "Gastrocnemius",
        "group": "leg_posterior",
        "heads": ["medial", "lateral"],
        "origin": "femoral_condyles",
        "insertion": "calcaneus_via_achilles_tendon",
        "action": "plantar_flexes_foot",
        "innervation": "tibial_nerve"
    },
    "soleus": {
        "id": 33,
        "name": "Soleus",
        "group": "leg_posterior",
        "origin": "tibia_fibula",
        "insertion": "calcaneus_via_achilles_tendon",
        "action": "plantar_flexes_foot",
        "innervation": "tibial_nerve"
    },
    "tibialis_anterior": {
        "id": 34,
        "name": "Tibialis Anterior",
        "group": "leg_anterior",
        "action": "dorsiflexes_inverts_foot",
        "innervation": "deep_fibular_nerve"
    }
}

# Layer 04: Nerves
NERVES = {
    # Cranial Nerves
    "olfactory_nerve": {
        "id": 1,
        "name": "Olfactory Nerve (CN I)",
        "type": "sensory",
        "function": "smell",
        "origin": "olfactory_epithelium",
        "destination": "olfactory_bulb"
    },
    "optic_nerve": {
        "id": 2,
        "name": "Optic Nerve (CN II)",
        "type": "sensory",
        "function": "vision",
        "origin": "retina",
        "destination": "thalamus"
    },
    "oculomotor_nerve": {
        "id": 3,
        "name": "Oculomotor Nerve (CN III)",
        "type": "motor",
        "function": "eye_movement_pupil_constriction",
        "origin": "midbrain"
    },
    "trochlear_nerve": {
        "id": 4,
        "name": "Trochlear Nerve (CN IV)",
        "type": "motor",
        "function": "superior_oblique_muscle",
        "origin": "midbrain"
    },
    "trigeminal_nerve": {
        "id": 5,
        "name": "Trigeminal Nerve (CN V)",
        "type": "mixed",
        "branches": ["ophthalmic", "maxillary", "mandibular"],
        "function": "facial_sensation_mastication"
    },
    "abducens_nerve": {
        "id": 6,
        "name": "Abducens Nerve (CN VI)",
        "type": "motor",
        "function": "lateral_rectus_muscle",
        "origin": "pons"
    },
    "facial_nerve": {
        "id": 7,
        "name": "Facial Nerve (CN VII)",
        "type": "mixed",
        "function": "facial_expression_taste_anterior_tongue",
        "origin": "pons"
    },
    "vestibulocochlear_nerve": {
        "id": 8,
        "name": "Vestibulocochlear Nerve (CN VIII)",
        "type": "sensory",
        "function": "hearing_balance",
        "origin": "inner_ear"
    },
    "glossopharyngeal_nerve": {
        "id": 9,
        "name": "Glossopharyngeal Nerve (CN IX)",
        "type": "mixed",
        "function": "taste_pharynx_sensation",
        "origin": "medulla"
    },
    "vagus_nerve": {
        "id": 10,
        "name": "Vagus Nerve (CN X)",
        "type": "mixed",
        "function": "parasympathetic_thorax_abdomen",
        "origin": "medulla",
        "notes": "Longest cranial nerve"
    },
    "accessory_nerve": {
        "id": 11,
        "name": "Accessory Nerve (CN XI)",
        "type": "motor",
        "function": "sternocleidomastoid_trapezius",
        "origin": "medulla_spinal_cord"
    },
    "hypoglossal_nerve": {
        "id": 12,
        "name": "Hypoglossal Nerve (CN XII)",
        "type": "motor",
        "function": "tongue_movement",
        "origin": "medulla"
    },
    # Spinal Nerves and Plexuses
    "cervical_plexus": {
        "id": 13,
        "name": "Cervical Plexus",
        "spinal_nerves": "C1-C4",
        "major_branches": ["phrenic_nerve"],
        "function": "neck_diaphragm"
    },
    "brachial_plexus": {
        "id": 14,
        "name": "Brachial Plexus",
        "spinal_nerves": "C5-T1",
        "major_branches": ["axillary_nerve", "musculocutaneous_nerve", "radial_nerve", "median_nerve", "ulnar_nerve"],
        "function": "upper_limb"
    },
    "lumbar_plexus": {
        "id": 15,
        "name": "Lumbar Plexus",
        "spinal_nerves": "L1-L4",
        "major_branches": ["femoral_nerve", "obturator_nerve"],
        "function": "lower_limb_anterior_thigh"
    },
    "sacral_plexus": {
        "id": 16,
        "name": "Sacral Plexus",
        "spinal_nerves": "L4-S4",
        "major_branches": ["sciatic_nerve", "pudendal_nerve"],
        "function": "lower_limb_pelvis"
    },
    "phrenic_nerve": {
        "id": 17,
        "name": "Phrenic Nerve",
        "type": "motor",
        "function": "diaphragm_innervation",
        "origin": "cervical_plexus_c3_c4_c5",
        "notes": "Keeps the diaphragm alive"
    },
    "axillary_nerve": {
        "id": 18,
        "name": "Axillary Nerve",
        "type": "mixed",
        "function": "deltoid_teres_minor",
        "origin": "brachial_plexus"
    },
    "musculocutaneous_nerve": {
        "id": 19,
        "name": "Musculocutaneous Nerve",
        "type": "mixed",
        "function": "anterior_arm_muscles",
        "origin": "brachial_plexus"
    },
    "radial_nerve": {
        "id": 20,
        "name": "Radial Nerve",
        "type": "mixed",
        "function": "posterior_arm_forearm_extensors",
        "origin": "brachial_plexus"
    },
    "median_nerve": {
        "id": 21,
        "name": "Median Nerve",
        "type": "mixed",
        "function": "anterior_forearm_hand",
        "origin": "brachial_plexus"
    },
    "ulnar_nerve": {
        "id": 22,
        "name": "Ulnar Nerve",
        "type": "mixed",
        "function": "intrinsic_hand_muscles",
        "origin": "brachial_plexus"
    },
    "femoral_nerve": {
        "id": 28,
        "name": "Femoral Nerve",
        "type": "mixed",
        "function": "quadriceps_anterior_thigh",
        "origin": "lumbar_plexus"
    },
    "sciatic_nerve": {
        "id": 31,
        "name": "Sciatic Nerve",
        "type": "mixed",
        "function": "posterior_thigh_leg_foot",
        "origin": "sacral_plexus",
        "notes": "Largest nerve in body"
    },
    "tibial_nerve": {
        "id": 32,
        "name": "Tibial Nerve",
        "type": "mixed",
        "function": "posterior_leg_plantar_foot",
        "origin": "sciatic_nerve"
    },
    "common_fibular_nerve": {
        "id": 33,
        "name": "Common Fibular (Peroneal) Nerve",
        "type": "mixed",
        "function": "anterior_lateral_leg",
        "origin": "sciatic_nerve"
    },
    "pudendal_nerve": {
        "id": 37,
        "name": "Pudendal Nerve",
        "type": "mixed",
        "function": "perineum_external_genitalia",
        "origin": "sacral_plexus"
    },
    "sympathetic_trunk": {
        "id": 38,
        "name": "Sympathetic Trunk",
        "type": "autonomic",
        "function": "sympathetic_nervous_system",
        "notes": "Runs parallel to spinal cord"
    }
}

# Layer 07: Blood Vessels
BLOOD_VESSELS = {
    # Arteries
    "ascending_aorta": {
        "id": 1,
        "name": "Ascending Aorta",
        "type": "artery",
        "origin": "left_ventricle",
        "branches": ["coronary_arteries"],
        "growth_stages": {
            "birth": {"length_cm": 2, "width_cm": 0.8, "circumference_cm": 2.5},
            "10_years": {"length_cm": 4, "width_cm": 1.5, "circumference_cm": 4.7},
            "adulthood": {"length_cm": 5, "width_cm": 3, "circumference_cm": 9.4}
        }
    },
    "aortic_arch": {
        "id": 2,
        "name": "Aortic Arch",
        "type": "artery",
        "branches": ["brachiocephalic_artery", "left_common_carotid_artery", "left_subclavian_artery"]
    },
    "descending_thoracic_aorta": {
        "id": 3,
        "name": "Descending Thoracic Aorta",
        "type": "artery",
        "branches": ["intercostal_arteries", "bronchial_arteries"]
    },
    "abdominal_aorta": {
        "id": 4,
        "name": "Abdominal Aorta",
        "type": "artery",
        "branches": ["celiac_trunk", "renal_arteries", "superior_mesenteric_artery", "inferior_mesenteric_artery"],
        "terminates_as": ["common_iliac_arteries"]
    },
    "pulmonary_artery": {
        "id": 7,
        "name": "Pulmonary Artery",
        "type": "artery",
        "origin": "right_ventricle",
        "function": "carries_deoxygenated_blood_to_lungs"
    },
    "coronary_artery": {
        "id": 9,
        "name": "Coronary Artery",
        "type": "artery",
        "origin": "ascending_aorta",
        "function": "supplies_heart_muscle"
    },
    "brachiocephalic_artery": {
        "id": 11,
        "name": "Brachiocephalic Artery",
        "type": "artery",
        "branches": ["right_common_carotid_artery", "right_subclavian_artery"]
    },
    "left_common_carotid_artery": {
        "id": 12,
        "name": "Left Common Carotid Artery",
        "type": "artery",
        "branches": ["internal_carotid_artery", "external_carotid_artery"],
        "function": "supplies_brain_and_face"
    },
    "right_common_carotid_artery": {
        "id": 13,
        "name": "Right Common Carotid Artery",
        "type": "artery",
        "function": "supplies_brain_and_face"
    },
    "subclavian_artery": {
        "id": 18,
        "name": "Subclavian Artery",
        "type": "artery",
        "branches": ["vertebral_artery", "axillary_artery"]
    },
    "axillary_artery": {
        "id": 20,
        "name": "Axillary Artery",
        "type": "artery",
        "continuation_of": "subclavian_artery",
        "becomes": "brachial_artery"
    },
    "brachial_artery": {
        "id": 22,
        "name": "Brachial Artery",
        "type": "artery",
        "branches": ["radial_artery", "ulnar_artery"],
        "notes": "Used for blood pressure measurement"
    },
    "radial_artery": {
        "id": 24,
        "name": "Radial Artery",
        "type": "artery",
        "notes": "Common site for pulse check"
    },
    "ulnar_artery": {
        "id": 26,
        "name": "Ulnar Artery",
        "type": "artery"
    },
    "celiac_trunk": {
        "id": 31,
        "name": "Celiac Trunk",
        "type": "artery",
        "branches": ["hepatic_artery", "splenic_artery", "left_gastric_artery"],
        "function": "supplies_liver_spleen_stomach"
    },
    "hepatic_artery": {
        "id": 32,
        "name": "Hepatic Artery",
        "type": "artery",
        "function": "supplies_liver"
    },
    "renal_artery": {
        "id": 35,
        "name": "Renal Artery",
        "type": "artery",
        "function": "supplies_kidneys"
    },
    "femoral_artery": {
        "id": 47,
        "name": "Femoral Artery",
        "type": "artery",
        "continuation_of": "external_iliac_artery",
        "becomes": "popliteal_artery",
        "notes": "Major artery of thigh"
    },
    "popliteal_artery": {
        "id": 49,
        "name": "Popliteal Artery",
        "type": "artery",
        "branches": ["anterior_tibial_artery", "posterior_tibial_artery"]
    },
    # Veins
    "superior_vena_cava": {
        "id": 5,
        "name": "Superior Vena Cava",
        "type": "vein",
        "drains_to": "right_atrium",
        "formed_by": ["brachiocephalic_veins"]
    },
    "inferior_vena_cava": {
        "id": 6,
        "name": "Inferior Vena Cava",
        "type": "vein",
        "drains_to": "right_atrium",
        "function": "returns_blood_from_lower_body"
    },
    "pulmonary_vein": {
        "id": 8,
        "name": "Pulmonary Vein",
        "type": "vein",
        "function": "carries_oxygenated_blood_from_lungs_to_left_atrium",
        "notes": "Only veins carrying oxygenated blood"
    },
    "cardiac_vein": {
        "id": 10,
        "name": "Cardiac Vein",
        "type": "vein",
        "function": "drains_heart_muscle"
    },
    "internal_jugular_vein": {
        "id": 16,
        "name": "Internal Jugular Vein",
        "type": "vein",
        "function": "drains_brain"
    },
    "external_jugular_vein": {
        "id": 17,
        "name": "External Jugular Vein",
        "type": "vein",
        "function": "drains_face_scalp"
    },
    "subclavian_vein": {
        "id": 19,
        "name": "Subclavian Vein",
        "type": "vein"
    },
    "hepatic_vein": {
        "id": 33,
        "name": "Hepatic Vein",
        "type": "vein",
        "drains": "liver_to_inferior_vena_cava"
    },
    "hepatic_portal_vein": {
        "id": 34,
        "name": "Hepatic Portal Vein",
        "type": "vein",
        "function": "carries_blood_from_gut_to_liver",
        "notes": "Part of portal system"
    },
    "renal_vein": {
        "id": 36,
        "name": "Renal Vein",
        "type": "vein",
        "drains": "kidneys"
    },
    "femoral_vein": {
        "id": 48,
        "name": "Femoral Vein",
        "type": "vein",
        "drains": "thigh_leg"
    },
    "great_saphenous_vein": {
        "id": 55,
        "name": "Great Saphenous Vein",
        "type": "vein",
        "notes": "Longest vein in body, used for grafts"
    }
}

# Layer 05: Organs
ORGANS = {
    "brain": {
        "id": 1,
        "name": "Brain",
        "system": "nervous",
        "weight_adult_g": 1300,
        "growth_stages": {
            "birth": {"length_cm": 10, "width_cm": 8, "circumference_cm": 34, "weight_g": 350},
            "10_years": {"length_cm": 14, "width_cm": 11, "circumference_cm": 52, "weight_g": 1200},
            "adulthood": {"length_cm": 15, "width_cm": 14, "circumference_cm": 55, "weight_g": 1300}
        },
        "regions": ["cerebrum", "cerebellum", "brainstem", "diencephalon"]
    },
    "spinal_cord": {
        "id": 2,
        "name": "Spinal Cord",
        "system": "nervous",
        "length_adult_cm": 45,
        "segments": 31
    },
    "heart": {
        "id": 3,
        "name": "Heart",
        "system": "cardiovascular",
        "weight_adult_g": 300,
        "growth_stages": {
            "birth": {"length_cm": 3, "width_cm": 2.5, "circumference_cm": 8, "weight_g": 20},
            "10_years": {"length_cm": 9, "width_cm": 6, "circumference_cm": 18, "weight_g": 150},
            "adulthood": {"length_cm": 12, "width_cm": 8.5, "circumference_cm": 25, "weight_g": 300}
        },
        "chambers": ["right_atrium", "right_ventricle", "left_atrium", "left_ventricle"]
    },
    "left_lung": {
        "id": 4,
        "name": "Left Lung",
        "system": "respiratory",
        "lobes": 2,
        "notes": "Smaller due to heart"
    },
    "right_lung": {
        "id": 5,
        "name": "Right Lung",
        "system": "respiratory",
        "lobes": 3
    },
    "liver": {
        "id": 6,
        "name": "Liver",
        "system": "digestive",
        "weight_adult_g": 1500,
        "growth_stages": {
            "birth": {"length_cm": 6, "width_cm": 4, "circumference_cm": 15, "weight_g": 120},
            "10_years": {"length_cm": 15, "width_cm": 10, "circumference_cm": 35, "weight_g": 800},
            "adulthood": {"length_cm": 20, "width_cm": 15, "circumference_cm": 45, "weight_g": 1500}
        },
        "functions": ["detoxification", "bile_production", "metabolism", "storage"]
    },
    "gallbladder": {
        "id": 7,
        "name": "Gallbladder",
        "system": "digestive",
        "function": "stores_bile"
    },
    "stomach": {
        "id": 8,
        "name": "Stomach",
        "system": "digestive",
        "capacity_adult_ml": 1000,
        "function": "mechanical_chemical_digestion"
    },
    "spleen": {
        "id": 9,
        "name": "Spleen",
        "system": "lymphatic",
        "function": "blood_filter_immune_response"
    },
    "pancreas": {
        "id": 10,
        "name": "Pancreas",
        "system": ["digestive", "endocrine"],
        "functions": ["enzyme_production", "insulin_glucagon_production"]
    },
    "small_intestine": {
        "id": 11,
        "name": "Small Intestine",
        "system": "digestive",
        "length_adult_m": 6,
        "sections": ["duodenum", "jejunum", "ileum"]
    },
    "large_intestine": {
        "id": 12,
        "name": "Large Intestine",
        "system": "digestive",
        "length_adult_m": 1.5,
        "sections": ["cecum", "colon", "rectum"]
    },
    "appendix": {
        "id": 13,
        "name": "Appendix",
        "system": "lymphatic",
        "notes": "Possible immune function"
    },
    "left_kidney": {
        "id": 14,
        "name": "Left Kidney",
        "system": "urinary",
        "function": "filtration_blood_pressure_regulation"
    },
    "right_kidney": {
        "id": 15,
        "name": "Right Kidney",
        "system": "urinary"
    },
    "urinary_bladder": {
        "id": 16,
        "name": "Urinary Bladder",
        "system": "urinary",
        "capacity_adult_ml": 500
    },
    "skin": {
        "id": 19,
        "name": "Skin",
        "system": "integumentary",
        "area_adult_m2": 2,
        "layers": ["epidermis", "dermis", "hypodermis"]
    },
    "thyroid_gland": {
        "id": 20,
        "name": "Thyroid Gland",
        "system": "endocrine",
        "hormones": ["thyroxine_t4", "triiodothyronine_t3", "calcitonin"]
    },
    "adrenal_glands": {
        "id": 22,
        "name": "Adrenal Glands",
        "system": "endocrine",
        "parts": ["adrenal_cortex", "adrenal_medulla"],
        "hormones": ["cortisol", "aldosterone", "adrenaline"]
    },
    "pituitary_gland": {
        "id": 23,
        "name": "Pituitary Gland",
        "system": "endocrine",
        "nickname": "master_gland",
        "parts": ["anterior", "posterior"]
    },
    "pineal_gland": {
        "id": 24,
        "name": "Pineal Gland",
        "system": "endocrine",
        "hormone": "melatonin"
    },
    "thymus": {
        "id": 25,
        "name": "Thymus",
        "system": ["lymphatic", "endocrine"],
        "function": "t_cell_maturation",
        "notes": "Larger in children"
    },
    "eye": {
        "id": 35,
        "name": "Eye",
        "system": "sensory",
        "components": ["cornea", "iris", "lens", "retina", "optic_nerve"]
    },
    "ear": {
        "id": 36,
        "name": "Ear",
        "system": "sensory",
        "sections": ["outer_ear", "middle_ear", "inner_ear"]
    }
}

# Ligaments and Tendons
LIGAMENTS_TENDONS = {
    "achilles_tendon": {
        "id": 1,
        "name": "Achilles Tendon",
        "type": "tendon",
        "connects": ["gastrocnemius", "soleus", "calcaneus"],
        "notes": "Strongest tendon in body"
    },
    "patellar_tendon": {
        "id": 2,
        "name": "Patellar Tendon",
        "type": "tendon",
        "connects": ["quadriceps", "tibia"],
        "notes": "Actually a ligament connecting patella to tibia"
    },
    "quadriceps_tendon": {
        "id": 3,
        "name": "Quadriceps Tendon",
        "type": "tendon",
        "connects": ["quadriceps_femoris", "patella"]
    },
    "biceps_brachii_tendon": {
        "id": 4,
        "name": "Biceps Brachii Tendon",
        "type": "tendon",
        "connects": ["biceps_brachii", "radial_tuberosity"]
    },
    "triceps_brachii_tendon": {
        "id": 5,
        "name": "Triceps Brachii Tendon",
        "type": "tendon",
        "connects": ["triceps_brachii", "olecranon"]
    },
    "acl": {
        "id": 12,
        "name": "Anterior Cruciate Ligament (ACL)",
        "type": "ligament",
        "location": "knee",
        "connects": ["femur", "tibia"],
        "function": "prevents_anterior_tibial_translation",
        "injury_common": True
    },
    "pcl": {
        "id": 13,
        "name": "Posterior Cruciate Ligament (PCL)",
        "type": "ligament",
        "location": "knee",
        "connects": ["femur", "tibia"],
        "function": "prevents_posterior_tibial_translation"
    },
    "mcl": {
        "id": 14,
        "name": "Medial Collateral Ligament (MCL)",
        "type": "ligament",
        "location": "knee",
        "function": "prevents_valgus_deformation"
    },
    "lcl": {
        "id": 15,
        "name": "Lateral Collateral Ligament (LCL)",
        "type": "ligament",
        "location": "knee",
        "function": "prevents_varus_deformation"
    },
    "rotator_cuff_tendons": {
        "id": "combined",
        "name": "Rotator Cuff Tendons",
        "type": "tendon_group",
        "components": ["supraspinatus_tendon", "infraspinatus_tendon", "teres_minor_tendon", "subscapularis_tendon"],
        "function": "stabilize_shoulder_joint"
    },
    "atfl": {
        "id": 36,
        "name": "Anterior Talofibular Ligament (ATFL)",
        "type": "ligament",
        "location": "ankle",
        "function": "prevents_anterior_talar_displacement",
        "notes": "Most commonly injured ankle ligament"
    }
}

# Endocrine System
ENDOCRINE = {
    "hypothalamus": {
        "id": 1,
        "name": "Hypothalamus",
        "location": "brain_below_thalamus",
        "function": "master_control_center",
        "hormones": ["gnrh", "trh", "crh", "dopamine", "oxytocin", "adh"],
        "notes": "Links nervous and endocrine systems"
    },
    "anterior_pituitary": {
        "id": 2,
        "name": "Anterior Pituitary Gland",
        "hormones": ["fsh", "lh", "acth", "tsh", "growth_hormone", "prolactin"],
        "notes": "Adenohypophysis"
    },
    "posterior_pituitary": {
        "id": 3,
        "name": "Posterior Pituitary Gland",
        "hormones": ["oxytocin", "adh"],
        "notes": "Neurohypophysis - stores hormones from hypothalamus"
    },
    "pineal_gland": {
        "id": 4,
        "name": "Pineal Gland",
        "hormones": ["melatonin"],
        "function": "circadian_rhythm_regulation"
    },
    "thyroid_gland": {
        "id": 5,
        "name": "Thyroid Gland",
        "hormones": ["t3", "t4", "calcitonin"],
        "function": "metabolism_calcium_regulation"
    },
    "parathyroid_glands": {
        "id": 6,
        "name": "Parathyroid Glands",
        "count": 4,
        "hormones": ["parathyroid_hormone_pth"],
        "function": "calcium_regulation"
    },
    "adrenal_cortex": {
        "id": 7,
        "name": "Adrenal Cortex",
        "hormones": ["cortisol", "aldosterone", "androgens"],
        "function": "stress_response_electrolyte_balance"
    },
    "adrenal_medulla": {
        "id": 8,
        "name": "Adrenal Medulla",
        "hormones": ["epinephrine", "norepinephrine"],
        "function": "fight_or_flight"
    },
    "pancreas_islets": {
        "id": 9,
        "name": "Pancreas (Islets of Langerhans)",
        "hormones": ["insulin", "glucagon", "somatostatin"],
        "function": "blood_glucose_regulation"
    },
    "ovaries": {
        "id": 10,
        "name": "Ovaries",
        "hormones": ["estrogen", "progesterone", "inhibin"],
        "function": "female_reproduction"
    },
    "testes": {
        "id": 11,
        "name": "Testes",
        "hormones": ["testosterone", "inhibin"],
        "function": "male_reproduction"
    },
    "thymus": {
        "id": 12,
        "name": "Thymus",
        "hormones": ["thymosin", "thymopoietin"],
        "function": "t_cell_development"
    }
}

# Lymphatic System
LYMPHATIC = {
    "thoracic_duct": {
        "id": 1,
        "name": "Thoracic Duct",
        "function": "main_lymphatic_vessel",
        "drains": "lower_body_left_upper_body",
        "empties_into": "left_subclavian_vein"
    },
    "right_lymphatic_duct": {
        "id": 2,
        "name": "Right Lymphatic Duct",
        "drains": "right_upper_body",
        "empties_into": "right_subclavian_vein"
    },
    "cisterna_chyli": {
        "id": 3,
        "name": "Cisterna Chyli",
        "function": "lymph_reservoir",
        "location": "abdomen"
    },
    "cervical_lymph_nodes": {
        "id": 4,
        "name": "Cervical Lymph Nodes",
        "location": "neck",
        "function": "filter_lymph_from_head_neck"
    },
    "axillary_lymph_nodes": {
        "id": 5,
        "name": "Axillary Lymph Nodes",
        "location": "armpit",
        "function": "filter_lymph_from_arm_breast"
    },
    "inguinal_lymph_nodes": {
        "id": 6,
        "name": "Inguinal Lymph Nodes",
        "location": "groin",
        "function": "filter_lymph_from_leg"
    },
    "spleen": {
        "id": 10,
        "name": "Spleen",
        "function": "blood_filter_immune_response",
        "location": "left_upper_abdomen"
    },
    "thymus": {
        "id": 11,
        "name": "Thymus",
        "function": "t_cell_maturation",
        "location": "mediastinum"
    },
    "red_bone_marrow": {
        "id": 12,
        "name": "Red Bone Marrow",
        "function": "blood_cell_production",
        "location": "spongy_bone"
    },
    "palatine_tonsils": {
        "id": 13,
        "name": "Palatine Tonsils",
        "location": "oropharynx",
        "function": "immune_defense"
    },
    "peyers_patches": {
        "id": 16,
        "name": "Peyer's Patches",
        "location": "small_intestine",
        "function": "gut_associated_lymphoid_tissue"
    }
}

# Growth Timeline
GROWTH_TIMELINE = {
    "week_0": {
        "stage": "Fertilization",
        "age": "Week 0 (Conception)",
        "milestones": ["Zygote formation", "Rapid cellular division begins"],
        "systems": ["N/A"]
    },
    "week_3": {
        "stage": "Embryonic Period",
        "age": "Week 3",
        "milestones": ["Neural tube formation", "Primitive heart tube develops"],
        "systems": ["Nerves", "Blood Vessels", "Organs"]
    },
    "week_4": {
        "stage": "Embryonic Period",
        "age": "Week 4",
        "milestones": ["Heart begins to beat", "Upper and lower limb buds appear"],
        "systems": ["Organs", "Blood Vessels", "Bones (Precursors)"]
    },
    "week_6_to_8": {
        "stage": "Embryonic Period",
        "age": "Week 6 to 8",
        "milestones": ["Cartilage models of bones form", "Major organ formation (organogenesis)", "Basic muscle blocks form"],
        "systems": ["Bones", "Organs", "Muscles"]
    },
    "week_9_to_12": {
        "stage": "Early Fetal Period",
        "age": "Week 9 to 12",
        "milestones": ["Primary ossification centers form", "Joint cavities begin to form"],
        "systems": ["Bones", "Joints", "Organs"]
    },
    "month_4_to_6": {
        "stage": "Mid Fetal Period",
        "age": "Month 4 to 6",
        "milestones": ["Muscle movements begin (quickening)", "Nervous system matures", "Lungs begin to produce surfactant"],
        "systems": ["Muscles", "Nerves", "Organs"]
    },
    "month_7_to_9": {
        "stage": "Late Fetal Period",
        "age": "Month 7 to 9",
        "milestones": ["Rapid brain growth", "Fat accumulation", "Functional maturation of organs for ex-utero life"],
        "systems": ["Nerves", "Organs"]
    },
    "birth": {
        "stage": "Neonatal",
        "age": "Birth (0 Years)",
        "milestones": ["Cardiovascular transition (foramen ovale closes)", "Independent respiration begins"],
        "systems": ["Blood Vessels", "Organs"]
    },
    "1_to_2_years": {
        "stage": "Infancy/Toddlerhood",
        "age": "1 to 2 Years",
        "milestones": ["Secondary ossification centers develop", "Rapid synaptogenesis in brain", "Gross motor skills development"],
        "systems": ["Bones", "Nerves", "Muscles"]
    },
    "3_to_11_years": {
        "stage": "Childhood",
        "age": "3 to 11 Years",
        "milestones": ["Continual long bone growth via active epiphyseal plates", "Muscle fiber hypertrophy", "Primary teeth replacement"],
        "systems": ["Bones", "Muscles", "Organs"]
    },
    "12_to_18_years": {
        "stage": "Adolescence (Puberty)",
        "age": "12 to 18 Years",
        "milestones": ["Endocrine hormonal surges", "Peak bone mass development", "Sexual dimorphism in muscle mass"],
        "systems": ["Endocrine", "Bones", "Muscles"]
    },
    "18_to_25_years": {
        "stage": "Early Adulthood",
        "age": "18 to 25 Years",
        "milestones": ["Epiphyseal plates close", "Peak muscle mass achieved", "Prefrontal cortex maturation"],
        "systems": ["Bones", "Muscles", "Nerves"]
    },
    "25_plus_years": {
        "stage": "Adulthood",
        "age": "25+ Years",
        "milestones": ["Peak physiological baseline", "Continuous bone remodeling", "Cellular maintenance across all systems"],
        "systems": ["All Systems"]
    }
}