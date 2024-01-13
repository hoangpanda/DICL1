from collections import defaultdict


def compute(session_item, session_bundle, predictions):
    session_precision = 0
    session_recall = 0
    coverage_item = 0
    all_hitted_bundle = 0
    for test_id, pred in predictions.items():
        if len(pred) == 0:
            continue
        all_items =  session_item[test_id].split(',')
        all_bundle = session_bundle[test_id]
        hitted_bundle = 0
        for bid, content in pred.items():
            try:
                reidx_items = set([all_items[int(i[-1])-1] for i in content])
            except Exception as e:
                print(test_id)
            for bundle in all_bundle:
                bundle_list = set(bundle[-1].split(','))
                if reidx_items <= bundle_list: 
                    hitted_bundle += 1
                    union_items = len(bundle_list & reidx_items)
                    coverage_item += union_items / len(bundle_list)
                    all_hitted_bundle += 1
                    break
        session_precision += hitted_bundle / len(pred)
        session_recall += hitted_bundle / len(all_bundle)
    
    session_precision /= len(predictions)
    session_recall /= len(predictions)
    coverage = coverage_item / all_hitted_bundle

    return session_precision, session_recall, coverage

def findErrors (session_id, generated_bundles, session_bundles, session_items):
    # feedback_dict = {0:[], 1:[], 2:[], 3:[], 4:[], 5:str} # 5: unexcepted error
    feedback_dict = defaultdict(list)
    groundtruth_bundles = session_bundles[session_id]
    all_items_session = session_items[session_id].split(',')
    for bid, items in generated_bundles.items():  
        if type(items) == str:
            items = [items]
        # find the neareast groundtruth
        all_similarity = []
        try:
            idx_items = set([all_items_session[int(item[-1])-1] for item in items])
        except Exception as e:
            # print(e)
            # print(session_id)
            feedback_dict[5].append(bid)
            continue
        for bundle in groundtruth_bundles:
            sim_score = len(idx_items&set(bundle[-1].split(','))) / len(idx_items|set(bundle[-1].split(',')))
            all_similarity.append(sim_score)
        index, max_score = max(enumerate(all_similarity), key=lambda pair: pair[1])
        if max_score == 0:
            feedback_dict[1].append(bid)
        elif max_score == 1:
            feedback_dict[0].append(bid)
        else:
            GT_bundle = set(groundtruth_bundles[index][-1].split(','))
            if idx_items <= GT_bundle:
                if len(idx_items) == 1:
                    feedback_dict[4].append(bid)
                else:
                    feedback_dict[3].append(bid)
            else:
                feedback_dict[2].append(bid)
    return feedback_dict