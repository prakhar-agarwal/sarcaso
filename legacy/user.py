import relations

class user():
    
    screen_name = ''
    subject_list = {}

    def get_screen_name(self):
        return self.screen_name

    def set_screen_name(self, sname):
        self.screen_name = sname
        return self.screen_name

    def get_subject_list(self):
        return self.subject_list

    def create_subject_list(self, data):

        data_type = str(type(data))

        if data_type == "<type 'list'>":
            for d in data:
                dic_rel = relations.get_dict_relations(d)
                for nounkey in dic_rel.keys():

                    if nounkey in self.subject_list.keys():
                        for pairs in dic_rel[nounkey]:
                            self.subject_list[nounkey].append(pairs)

                    else:
                        self.subject_list[nounkey] = dic_rel[nounkey]


        elif data_type == "<type 'file'>":
            for line in data:
                dic_rel = relations.get_dict_relations(str(line))
                for nounkey in dic_rel.keys():

                    if nounkey in self.subject_list.keys():
                        for pairs in dic_rel[nounkey]:
                            self.subject_list[nounkey].append(pairs)

                    else:
                        self.subject_list[nounkey] = dic_rel[nounkey]


        return self.subject_list

