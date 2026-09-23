def build_profile(**profile):
    profile_list =[]
    for key, value in profile.items():
        profile_list.append(f"{key}: {value}")
    return '; '.join(profile_list)
   
print(build_profile(name='Ada', age=36))