class DBRouter (object):
  app_labels = {'pult4db', 'pult4db_archives'}

  def db_for_read(self, model, **hints):
    if model._meta.app_label == 'pult4db':
      return 'pult4db'
    if model._meta.app_label == 'pult4db_archives':
      return 'pult4db_archives'
    return 'pult4db'
  
  def db_for_write(self, model, **hints):
    if model._meta.app_label == 'pult4db':
      return 'pult4db'
    if model._meta.app_label == 'pult4db_archives':
      return 'pult4db_archives'
    return 'pult4db'
  
  def allow_relation(self, obj1, obj2, **hints):
    if (
      obj1._meta.app_label in self.app_labels
      or
      obj2._meta.app_label in self.app_labels
    ):
      return True
    return None
  